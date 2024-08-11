| title | sdk | sdk_version | app_file | tags | description |
|-------|-----|-------------|----------|------|-------------|
|reidentification_risk| | |reidentification_risk.py|`evaluate` `metric`| |

# Metric Card for reidentification_risk

## Metric Description

Reidentification Risk measures the likelihood that an individual in a dataset can be uniquely identified based on a specific unique identifier. This metric is crucial in assessing the privacy risk associated with publishing or sharing a dataset, particularly in cases where sensitive information is involved.

## Calculation Steps

1. **Data Sampling:** A random subset of 100 records is selected from the dataset. This step ensures the calculation is manageable while still being representative of the entire dataset.
2. **Unique Identifier Evaluation:** The number of unique values within the specified `unique_identifier` column is counted. This column should contain values that, if unique, could potentially identify individuals within the dataset.
3. **Total Records:** The total number of records in the sampled subset is determined.
4. **Risk Calculation:** The reidentification risk is calculated as the ratio of the number of unique identifiers to the total number of records in the subset. This ratio represents the proportion of records that can be uniquely identified based on the chosen identifier.

## How to Use

1. **Load and read data**

```python
real_data_path = "../数据/ZZZ_Sepsis_Data_From_R.csv"
synthetic_data_path = "../数据/YB003_DS"
```

2. **Create a DataMmparator object and call reidentification_risk() to get the reidentification_risk_value**

```python
Dc = DataComparator(real_data_path, synthetic_data_path)
unique_identifier = 'PatientID'
reidentification_risk_value = Dc.reidentification_risk(df_combined, unique_identifier)
print(f"Re-identification Risk: {reidentification_risk_value}")
>>> Re-identification Risk: 0.99
```

### Inputs

|input|type|desccription|
|-----|----|------------|
|unique_identifier|str|This column typically contains data that may be used to uniquely identify individuals, such as patient numbers, social security numbers (SSNs), etc. If most of the values in this column are unique, it may lead to a higher risk of re identification|
|df_combined|DataFrame|Dataset for inferring risk assessment|

### Output Values

The output is a dictionary containing the following fields:

|output|type|desccription|
|-----|----|------------|
|reidentification_risk_value|float|Represents the re identification risk calculated based on the given unique identifier column (unique_identifier). This value reflects the proportion of records in the sample that can be uniquely identified by a unique identifier|

## Examples

```python
real_data_path = "../数据/ZZZ_Sepsis_Data_From_R.csv"
synthetic_data_path = "../数据/YB003_DS"
Dc = DataComparator(real_data_path, synthetic_data_path)
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
unique_identifier = 'PatientID'
reidentification_risk_value = Dc.reidentification_risk(df_combined, unique_identifier)
print(f"Re-identification Risk: {reidentification_risk_value}")
>>> Re-identification Risk: 0.99
```

## Limitations and Bias

De-identification techniques (e.g., data masking, pseudonymisation, aggregation, etc.) are not foolproof. Attackers may use residual information (e.g., background knowledge) from de-identified data for re-identification. The effectiveness of de-identification techniques may be affected by the attacker's level of knowledge and other external data, thus increasing the risk of re-identification.

Highly accurate data (e.g., precise geographic location, detailed health records) is more likely to lead to re-identification than ambiguous data. Highly accurate data provides more information and may make it easier for an attacker to re-identify an individual with little background knowledge.

When data is combined with other data sources (e.g., through data linking techniques), additional information may be exposed, increasing the risk of re-identification. Even if the data is de-identified, the association with other data sources may enable an attacker to identify individuals, reducing the effectiveness of privacy protection.

## citation

[1] Zhang, Z., Li, X., & Zhang, Y. (2024). "A Comprehensive Review of Re-identification Risk in Data Privacy." In Journal of Privacy and Confidentiality.

[2] Patel, M., Singh, A., & Green, R. (2023). "Evaluating Re-identification Risks in De-identified Data: Advances and Challenges." In ACM Transactions on Privacy and Security.

[3] Anderson, J., Yu, K., & Kumar, S. (2023). "Mitigating Re-identification Risk in Healthcare Data: A Comparative Study." In Journal of Biomedical Informatics.
