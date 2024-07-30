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

# 再识别风险
def reidentification_risk(df, unique_identifier):
    df_subset = df.sample(n=100, random_state=42)
    unique_values = df_subset[unique_identifier].nunique()
    total_records = len(df_subset)
    risk = unique_values / total_records
    return risk

unique_identifier = 'PatientID'
reidentification_risk_value = reidentification_risk(df_combined, unique_identifier)
print(f"Re-identification Risk: {reidentification_risk_value}")
