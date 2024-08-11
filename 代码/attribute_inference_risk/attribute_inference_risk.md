| title | sdk | sdk_version | app_file | tags | description |
|-------|-----|-------------|----------|------|-------------|
|attribute_inference_risk| | |attribute_inference_risk.py|`evaluate` `metric`| |

# Metric Card for attribute_inference_risk

## Metric Description

Attribute Inference Risk is a metric used to evaluate the difficulty of inferring a specific attribute from other features within a dataset. It quantifies the potential risk associated with the predictability of a sensitive attribute when it is excluded from the dataset, thereby assessing how much information the other features provide about this attribute.

### Calculation Steps ###

1. **Sample Selection:** A random subset of 100 samples is selected from the original dataset to ensure a manageable and representative sample size.
2. **Feature Preparation:** The target attribute (the one being assessed for inference risk) is removed from the dataset, and the remaining features are retained for the analysis. The target attribute is then discretized into 5 categories using equal-frequency binning to enable classification.
3. **Data Filtering:** Only numerical features are retained from the remaining features, ensuring compatibility with the logistic regression model.
4. **Data Splitting:** The dataset is split into training and testing sets in a 1:1 ratio to allow for robust model evaluation.
5. **Model Training:** A logistic regression model is trained on the training data to predict the discretized target attribute.
6. **Risk Computation:** The model's accuracy on the test data is computed, and the attribute inference risk is calculated as `1 - accuracy`. A higher risk value indicates that the attribute is harder to infer, suggesting lower predictability from the other features.

## How to Use

1. **Load and read data**

```python
real_data_path = "../数据/ZZZ_Sepsis_Data_From_R.csv"
synthetic_data_path = "../数据/YB003_DS"
```

2. **Set specific attributes that require assessment and inference of risk**

```python
attribute = 'Age'
```

3. **Create a DataMmparator object and call attributis_reference_risk() to calculate the inference risk of the attribute**

```python
Dc = DataComparator(real_data_path, synthetic_data_path)
attribute_risk = Dc.attribute_inference_risk(df_combined, attribute)
    print(f"Attribute Inference Risk for {attribute}: {attribute_risk}")
```

### Inputs

|input|type|desccription|
|-----|----|------------|
|attribute|str|Names of specific attributes that require assessment and inference of risk|
|df_combined|DataFrame|Dataset for inferring risk assessment|

### Output Values

The output is a dictionary containing the following fields:
|output|type|desccription|
|-----|----|------------|
|attribute_risk|float|The inferred risk value of a specific attribute calculated. This value represents the difficulty of inferring this attribute from other features. The range of values is between 0 and 1. The higher the value, the greater the risk, indicating that the attribute is difficult to infer from other features|

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
attribute = 'Age'  # Example attribute
if attribute in df_combined.columns:
     attribute_risk = Dc.attribute_inference_risk(df_combined, attribute)
     print(f"Attribute Inference Risk for {attribute}: {attribute_risk}")
else:
     print(f"Attribute {attribute} not found in the data")
>>> Attribute Inference Risk for Age: 0.19999999999999996
```

## Limitations and Bias

The effectiveness of attribute inference attacks depends on the distribution of attributes in the training data. If some attributes in the training data are very sparse or unevenly distributed, it may be difficult for an attacker to accurately infer these attributes. Uneven data distribution may reduce the success rate of the attack and make attribute inference more difficult.

Attribute inference attacks may be less effective when data heterogeneity is high. For example, it may be difficult for an attacker to accurately infer attributes when there is a high degree of noise or outliers in the data. Data heterogeneity may make the inference results less reliable and affect the overall effectiveness of the attack.

If the model overfits the training data, an attacker may be able to exploit this overfitting for attribute inference. Overfitting makes the model overly sensitive to the features of the training data, which makes inference easier. Overfitting of the model may lead to biased inference results, especially if there are strong features in the training data.

## citation

[1] Nerini, M., & Zhang, L. (2023). "Evaluating Attribute Inference Risks in Machine Learning Models." In Proceedings of the 2023 IEEE Symposium on Security and Privacy (S&P 2023).

[2] Santos, D., & Liu, H. (2023). "Attribute Inference Attacks and Mitigation Strategies in Data Privacy." In Journal of Privacy and Confidentiality.

[3] Kim, J., & Chen, X. (2022). "Assessing Attribute Inference Risks in Federated Learning Systems." In ACM Transactions on Privacy and Security (TOPS).
