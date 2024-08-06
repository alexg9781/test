import pandas as pd
import numpy as np
import torch
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

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