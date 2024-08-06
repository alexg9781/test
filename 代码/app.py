import pandas as pd
import torch
from DataComparator import DataComparator

real_data_path = "../数据/ZZZ_Sepsis_Data_From_R.csv"
synthetic_data_path = "../数据/YB003_DS"
Dc = DataComparator(real_data_path, synthetic_data_path)

# pearson_results, spearman_results = Dc.correlation()
# # 第一个值：相关系数 第二个值：p值
# print(pd.DataFrame(pearson_results))

# group_col = 'Demo001_Gender'
# real_f_test_results, synthetic_f_test_results = Dc.ftest(group_col)
# print(pd.DataFrame(real_f_test_results))

# ks_test_results = Dc.ks_test()
# print(ks_test_results)

# group_col = 'Demo001_Gender'
# real_t_test_results, synthetic_t_test_results = Dc.ttest(group_col)
# print(pd.DataFrame(real_t_test_results))

# 读取CSV文件
df_fakehypotension = pd.read_csv('../数据/C001_FakeHypotension.csv')
df_fakesepsis = pd.read_csv('../数据/C001_FakeSepsis.csv')
df_sepsis_data = pd.read_csv('../数据/ZZZ_Sepsis_Data_From_R.csv')

# 读取非CSV文件
data = torch.load('../数据/YB003_DS', map_location=torch.device('cpu'))
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

# attribute = 'Age'  # Example attribute
# if attribute in df_combined.columns:
#     attribute_risk = Dc.attribute_inference_risk(df_combined, attribute)
#     print(f"Attribute Inference Risk for {attribute}: {attribute_risk}")
# else:
#     print(f"Attribute {attribute} not found in the data")

# euclidean_dist_matrix = Dc.calculate_euclidean_distances(df_subset)
# print(euclidean_dist_matrix)
# print("Euclidean Distances Calculated")

# membership_risk = Dc.membership_inference_risk(df_combined)
# print(f"Membership Inference Risk: {membership_risk}")

unique_identifier = 'PatientID'
reidentification_risk_value = Dc.reidentification_risk(df_combined, unique_identifier)
print(f"Re-identification Risk: {reidentification_risk_value}")