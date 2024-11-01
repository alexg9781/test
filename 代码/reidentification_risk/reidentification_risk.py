import pandas as pd
# 再识别风险
def reidentification_risk(df, unique_identifier):
    df_subset = df.sample(n=100, random_state=42)
    unique_values = df_subset[unique_identifier].nunique()
    total_records = len(df_subset)
    risk = unique_values / total_records
    return risk