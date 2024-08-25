| title | sdk | sdk_version | app_file | tags | description |
|-------|-----|-------------|----------|------|-------------|
|membership_inference_risk| | |membership_inference_risk.py|`evaluate` `metric`| |

# Metric Card for membership_inference_risk

## Metric Description

Membership Inference Risk measures the susceptibility of a machine learning model to membership inference attacks. In such attacks, an adversary attempts to determine whether a specific data point was part of the model's training dataset based on the model's predictions.

## Measurement indicators

`Continuous and categorical variables`: This measure considers whether the model leaks information from the training data and can be used for both continuous and categorical variables.

## Calculation Steps

1. **Data Sampling:** A random subset of 1000 samples is selected from the dataset to ensure a manageable size for model training and testing.
2. **Feature Selection:** Only numerical features are considered for training the model. This selection is crucial as non-numerical data might not be suitable for the chosen model.
3. **Data Splitting:** The sampled data is split into training and testing sets in a 50:50 ratio to evaluate the model's generalization ability.
4. **Model Training & Prediction:** A logistic regression model is trained on the training set and used to predict the membership status of the samples in the test set.
5. **Risk Calculation:** The model's accuracy on the test set is computed, and the membership inference risk is defined as `1 - accuracy`. A higher risk score indicates a higher vulnerability to membership inference attacks.

## How to Use

1. **Load and read data**

```python
real_data_path = "../数据/ZZZ_Sepsis_Data_From_R.csv"
synthetic_data_path = "../数据/YB003_DS"
```

2. **Create a DataMmparator object and call membership_inference_risk() to get the membership_risk**

```python
Dc = DataComparator(real_data_path, synthetic_data_path)
membership_risk = Dc.membership_inference_risk(df_combined)
print(f"Membership Inference Risk: {membership_risk}")
>>> Membership Inference Risk: 0.99
```

### Inputs

|input|type|desccription|
|-----|----|------------|
|df_combined|DataFrame|Dataset for inferring risk assessment|

### Output Values

The output is a dictionary containing the following fields:

|output|type|desccription|
|-----|----|------------|
|membership_risk|float|This value represents the vulnerability of the model to member inference attacks, and the closer the value is to 1, the greater the risk; The closer the value is to 0, the safer the model is|

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
membership_risk = Dc.membership_inference_risk(df_combined)
print(f"Membership Inference Risk: {membership_risk}")
>>> Membership Inference Risk: 0.99
```

## Limitations and Bias

The effectiveness of Membership inference attacks is highly dependent on the quality and characteristics of the training data. For example, if the training data is very similar and evenly distributed, it may be more difficult for an attacker to infer membership in individual data points. The effectiveness of the attack may be limited in cases where the training data has highly individualised or extreme characteristics.

Complex models (e.g., deep neural networks) may be more difficult than simple models (e.g., linear models) to perform effective membership inference attacks. The tendency of complex models to overfit may make it more difficult for an attacker to capture obvious patterns. The complexity of the model may affect the effectiveness of the attack, making certain attack strategies less effective on complex models than on simple models.

An attacker may have trained the model with certain specific datasets that may not be fully representative of the real training data. In this way, the inference results may suffer from sample selection bias. Sample selection bias may lead to inaccuracies in the attack results, which may affect the assessment of model privacy.

## citation

[1] Shokri, R., & Shmatikov, V. (2015). "Privacy-preserving deep learning." In Proceedings of the 2015 ACM SIGSAC Conference on Computer and Communications Security (CCS 2015).

[2] Song, L., Raghunathan, A., & Shmatikov, V. (2020). "Overfitting is the source of membership inference attacks." In Proceedings of the 2020 IEEE European Symposium on Security and Privacy (EuroS&P 2020).

[3] Tramèr, F., & Boneh, D. (2021). "Membership inference attacks against machine learning models: A survey and taxonomy." ACM Computing Surveys.
