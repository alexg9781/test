import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
# 成员推断风险
def membership_inference_risk(df):
    df_subset = df.sample(n=1000, random_state=42)
    features = df_subset.select_dtypes(include=[np.number])
    labels = df_subset['PatientID']
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.5, random_state=42)

    clf = LogisticRegression(max_iter=100000,solver="liblinear")
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    risk = 1 - acc
    return risk