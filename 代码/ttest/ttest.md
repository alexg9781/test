| title | sdk | sdk_version | app_file | tags | description |
|-------|-----|-------------|----------|------|-------------|
|t-test| | |t-test.py|`evaluate` `metric`| |

# Metric Card for t-test

## Metric Description

The T-Test is a statistical method used to determine if there is a significant difference between the means of two groups. This metric is commonly used in hypothesis testing to compare the means of two independent samples to see if they are significantly different from each other.

## Measurement indicators

`Continuous variables`: T-test is used to compare whether there is a significant difference in the mean of continuous variables between two groups.

`Categorical variables`: applicable for grouping in binary variables (such as treatment group and control group). The categorical variables themselves are not the main test objects.

## Calculation Steps

1. **Data Selection:** The data is first filtered to include only numerical columns (`int64`, `float64`). For each column, the data is split into two groups based on the specified `group_col`.
2. **T-Test Execution:** A two-sample t-test (`ttest_ind`) is conducted for each numerical column, comparing the means of the two groups. This test assesses whether the means of the two groups are statistically different.
3. **Handling Missing Data:** If there are missing values in the data, they are omitted from the analysis using `nan_policy='omit'`.
4. **Results Storage:** The results of the t-test, including the t-statistic and p-value, are stored in a dictionary, where the key is the column name and the value is the test result.

## How to Use

1. **Load and read data**

```python
real_data_path = "../数据/ZZZ_Sepsis_Data_From_R.csv"
synthetic_data_path = "../数据/YB003_DS"
```

2. **Create a DataMmparator object and call reidentification_risk() to get the real_t_test_results, synthetic_t_test_results**

```python
Dc = DataComparator(real_data_path, synthetic_data_path)
group_col = 'Demo001_Gender'
real_t_test_results, synthetic_t_test_results = Dc.ttest(group_col)
print(pd.DataFrame(real_t_test_results))
>>> Loading file: ./数据/ZZZ_Sepsis_Data_From_R.csv Loading file: ./数据/YB003_DS -------------- 40 -------------- 30 -------------- 80 -------------- 100 -------------- 90 -------------- 10 -------------- 70 -------------- 50 -------------- 20 -------------- 60 Processing key: 40 Columns in DataFrame: RangeIndex(start=0, stop=600, step=1) Skipping key 40 because Demo001_Gender is not in columns Processing key: 30 Columns in DataFrame: RangeIndex(start=0, stop=450, step=1) Skipping key 30 because Demo001_Gender is not in columns Processing key: 80 Columns in DataFrame: RangeIndex(start=0, stop=1200, step=1) Skipping key 80 because Demo001_Gender is not in columns Processing key: 100 Columns in DataFrame: RangeIndex(start=0, stop=1500, step=1) Skipping key 100 because Demo001_Gender is not in columns Processing key: 90 Columns in DataFrame: RangeIndex(start=0, stop=1350, step=1) Skipping key 90 because Demo001_Gender is not in columns Processing key: 10 Columns in DataFrame: RangeIndex(start=0, stop=150, step=1) Skipping key 10 because Demo001_Gender is not in columns Processing key: 70 Columns in DataFrame: RangeIndex(start=0, stop=1050, step=1) Skipping key 70 because Demo001_Gender is not in columns Processing key: 50 Columns in DataFrame: RangeIndex(start=0, stop=750, step=1) Skipping key 50 because Demo001_Gender is not in columns Processing key: 20 Columns in DataFrame: RangeIndex(start=0, stop=300, step=1) Skipping key 20 because Demo001_Gender is not in columns Processing key: 60 Columns in DataFrame: RangeIndex(start=0, stop=900, step=1) Skipping key 60 because Demo001_Gender is not in columns Processing real_data Columns in real_data: <generator object DataFrame.items at 0x7fae0a69e2e0> t_test_result = ttest_ind(group1, group2, nan_policy='omit') Unnamed: 0 Admn001_ID Demo001_Gender Demo002_Age Demo003_ReAd Vitl001_GCS ... Flud005_Output4H Devr001_SOFA Devr002_SIRS Devr003_ShockIndex Devr004_PaFiRatio Devr005_FluidBalance 0 -4.165186 -4.194990 -inf -7.360762e+00 5.464317e+00 -4.264391 ... 1.137395e+01 2.210896 -2.251588 -2.651344 -3.864558 -1.648436 1 0.000031 0.000027 0.0 1.887744e-13 4.693368e-08 0.000020 ... 6.731314e-30 0.027052 0.024357 0.008022 0.000112 0.099276 [2 rows x 51 columns]
```

### Inputs

|input|type|desccription|
|-----|----|------------|
|real_data_path|str|The file path of a real dataset, usually a string containing the path to the CSV file or other format data file to be loaded|
|synthetic_data_path|str|The file path of the synthetic dataset, similar to the path of a real dataset, represents the storage location of the synthetic data|
|group_col|str|Used to define column names for two groups. This column is usually a categorical variable that divides data into two groups for comparison|

### Output Values

The output is a dictionary containing the following fields:

|output|type|desccription|
|-----|----|------------|
|real_t_test_results |dict|Store the t-test results for each numerical column. The key is the column name, and the value is the t-test result (p-value)|
|synthetic_t_test_results |dict|Store the t-test results for each numerical column. The key is the column name, and the value is the t-test result (p-value)|

## Examples

```python
real_data_path = "../数据/ZZZ_Sepsis_Data_From_R.csv"
synthetic_data_path = "../数据/YB003_DS"
Dc = DataComparator(real_data_path, synthetic_data_path)
group_col = 'Demo001_Gender'
real_t_test_results, synthetic_t_test_results = Dc.ttest(group_col)
print(pd.DataFrame(real_t_test_results))
>>> Loading file: ./数据/ZZZ_Sepsis_Data_From_R.csv Loading file: ./数据/YB003_DS -------------- 40 -------------- 30 -------------- 80 -------------- 100 -------------- 90 -------------- 10 -------------- 70 -------------- 50 -------------- 20 -------------- 60 Processing key: 40 Columns in DataFrame: RangeIndex(start=0, stop=600, step=1) Skipping key 40 because Demo001_Gender is not in columns Processing key: 30 Columns in DataFrame: RangeIndex(start=0, stop=450, step=1) Skipping key 30 because Demo001_Gender is not in columns Processing key: 80 Columns in DataFrame: RangeIndex(start=0, stop=1200, step=1) Skipping key 80 because Demo001_Gender is not in columns Processing key: 100 Columns in DataFrame: RangeIndex(start=0, stop=1500, step=1) Skipping key 100 because Demo001_Gender is not in columns Processing key: 90 Columns in DataFrame: RangeIndex(start=0, stop=1350, step=1) Skipping key 90 because Demo001_Gender is not in columns Processing key: 10 Columns in DataFrame: RangeIndex(start=0, stop=150, step=1) Skipping key 10 because Demo001_Gender is not in columns Processing key: 70 Columns in DataFrame: RangeIndex(start=0, stop=1050, step=1) Skipping key 70 because Demo001_Gender is not in columns Processing key: 50 Columns in DataFrame: RangeIndex(start=0, stop=750, step=1) Skipping key 50 because Demo001_Gender is not in columns Processing key: 20 Columns in DataFrame: RangeIndex(start=0, stop=300, step=1) Skipping key 20 because Demo001_Gender is not in columns Processing key: 60 Columns in DataFrame: RangeIndex(start=0, stop=900, step=1) Skipping key 60 because Demo001_Gender is not in columns Processing real_data Columns in real_data: <generator object DataFrame.items at 0x7fae0a69e2e0> t_test_result = ttest_ind(group1, group2, nan_policy='omit') Unnamed: 0 Admn001_ID Demo001_Gender Demo002_Age Demo003_ReAd Vitl001_GCS ... Flud005_Output4H Devr001_SOFA Devr002_SIRS Devr003_ShockIndex Devr004_PaFiRatio Devr005_FluidBalance 0 -4.165186 -4.194990 -inf -7.360762e+00 5.464317e+00 -4.264391 ... 1.137395e+01 2.210896 -2.251588 -2.651344 -3.864558 -1.648436 1 0.000031 0.000027 0.0 1.887744e-13 4.693368e-08 0.000020 ... 6.731314e-30 0.027052 0.024357 0.008022 0.000112 0.099276 [2 rows x 51 columns]
```

## Limitations and Bias

T-tests are very sensitive to outliers. Outliers can significantly affect the mean and variance, which in turn affects the results of the t-test. Outliers can cause bias in the t-test results, making the results inaccurate or even misleading.

The classical t-test is only used to compare means between two groups. If it is necessary to compare means between three or more groups, other statistical methods such as ANOVA must be used. When faced with multiple group comparisons, the use of multiple T-tests increases the risk of type I error and is therefore not suitable for multiple group comparison scenarios.

## citation

[1] Kim, T.-K. (2017). "T test as a parametric statistic." Korean Journal of Anesthesiology.

[2] Suresh, K. P., & Chandrashekara, S. (2012). "Sample size estimation and power analysis for clinical research studies." Journal of Human Reproductive Sciences.
