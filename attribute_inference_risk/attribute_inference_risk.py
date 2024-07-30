import pandas as pd
import numpy as np
import torch
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 读取CSV文件
df_fakehypotension = pd.read_csv('C001_FakeHypotension.csv')
df_fakesepsis = pd.read_csv('C001_FakeSepsis.csv')
df_sepsis_data = pd.read_csv('ZZZ_Sepsis_Data_From_R.csv')

# 读取非CSV文件
data = torch.load('YB003_DS', map_location=torch.device('cpu'))

# 合并数据
df_fakehypotension['PatientID'] = df_fakehypotension['PatientID'].astype(str) + '_hypo'
df_fakesepsis['PatientID'] = df_fakesepsis['PatientID'].astype(str) + '_sepsis'
df_sepsis_data['Admn001_ID'] = df_sepsis_data['Admn001_ID'].astype(str) + '_sepsis_data'

# 为了合并数据，需要确保列名一致
df_sepsis_data.rename(columns={'Admn001_ID': 'PatientID'}, inplace=True)

# 将所有数据合并为一个数据框
df_combined = pd.concat([df_fakehypotension, df_fakesepsis, df_sepsis_data], ignore_index=True)

# 处理缺失值，可以选择填充或删除
df_combined.fillna(df_combined.mean(numeric_only=True), inplace=True)

# 选择一个较小的数据子集来避免内存问题
df_subset = df_combined.sample(n=100, random_state=42)

# 属性推断风险
def attribute_inference_risk(df, attribute):
    df_subset = df.sample(n=100, random_state=42)
    features = df_subset.drop(columns=[attribute])
    target = pd.cut(df_subset[attribute], bins=5, labels=False)  # 将连续变量转换为分类变量，这里使用5个年龄段
    
    # 仅选择数值型数据
    features = features.select_dtypes(include=[np.number])
    
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.5, random_state=42)
    
    clf = LogisticRegression(max_iter=10000)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    risk = 1 - acc
    return risk

attribute = 'Age'  # Example attribute
if attribute in df_combined.columns:
    attribute_risk = attribute_inference_risk(df_combined, attribute)
    print(f"Attribute Inference Risk for {attribute}: {attribute_risk}")
else:
    print(f"Attribute {attribute} not found in the data")