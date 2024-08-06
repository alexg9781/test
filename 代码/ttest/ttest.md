| title | sdk | sdk_version | app_file | tags | description |
|-------|-----|-------------|----------|------|-------------|
|t-test| | |t-test.py|`evaluate` `metric`| |

# Metric Card for t-test

## Metric Description

See the [sacreBLEU README.md](https://github.com/khloe-S/test/tree/main/t-test) for more information.

## How to Use

1. **Install the related packages**

```python
pip install -r requirements.txt
```

2. **To run the t-test.py file or enter the following code in the terminal:**

```python
python ttest.py
```

```python
>>> real_data_path ="../数据/ZZZ_Sepsis_Data_From_R.csv"
>>> synthetic_data_path = "../数据/YB003_DS"
>>> group_col = 'Demo001_Gender'
>>> 
>>> analyzer = TTestAnalyzer(real_data_path, synthetic_data_path)
>>> real_t_test_results, synthetic_t_test_results = analyzer.analyze_tests(group_col)
>>> 
>>> print(pd.DataFrame(real_t_test_results))
>>> Loading file: ./数据/ZZZ_Sepsis_Data_From_R.csv Loading file: ./数据/YB003_DS -------------- 40 -------------- 30 -------------- 80 -------------- 100 -------------- 90 -------------- 10 -------------- 70 -------------- 50 -------------- 20 -------------- 60 Processing key: 40 Columns in DataFrame: RangeIndex(start=0, stop=600, step=1) Skipping key 40 because Demo001_Gender is not in columns Processing key: 30 Columns in DataFrame: RangeIndex(start=0, stop=450, step=1) Skipping key 30 because Demo001_Gender is not in columns Processing key: 80 Columns in DataFrame: RangeIndex(start=0, stop=1200, step=1) Skipping key 80 because Demo001_Gender is not in columns Processing key: 100 Columns in DataFrame: RangeIndex(start=0, stop=1500, step=1) Skipping key 100 because Demo001_Gender is not in columns Processing key: 90 Columns in DataFrame: RangeIndex(start=0, stop=1350, step=1) Skipping key 90 because Demo001_Gender is not in columns Processing key: 10 Columns in DataFrame: RangeIndex(start=0, stop=150, step=1) Skipping key 10 because Demo001_Gender is not in columns Processing key: 70 Columns in DataFrame: RangeIndex(start=0, stop=1050, step=1) Skipping key 70 because Demo001_Gender is not in columns Processing key: 50 Columns in DataFrame: RangeIndex(start=0, stop=750, step=1) Skipping key 50 because Demo001_Gender is not in columns Processing key: 20 Columns in DataFrame: RangeIndex(start=0, stop=300, step=1) Skipping key 20 because Demo001_Gender is not in columns Processing key: 60 Columns in DataFrame: RangeIndex(start=0, stop=900, step=1) Skipping key 60 because Demo001_Gender is not in columns Processing real_data Columns in real_data: <generator object DataFrame.items at 0x7fae0a69e2e0> t_test_result = ttest_ind(group1, group2, nan_policy='omit') Unnamed: 0 Admn001_ID Demo001_Gender Demo002_Age Demo003_ReAd Vitl001_GCS ... Flud005_Output4H Devr001_SOFA Devr002_SIRS Devr003_ShockIndex Devr004_PaFiRatio Devr005_FluidBalance 0 -4.165186 -4.194990 -inf -7.360762e+00 5.464317e+00 -4.264391 ... 1.137395e+01 2.210896 -2.251588 -2.651344 -3.864558 -1.648436 1 0.000031 0.000027 0.0 1.887744e-13 4.693368e-08 0.000020 ... 6.731314e-30 0.027052 0.024357 0.008022 0.000112 0.099276 [2 rows x 51 columns]
```

### Inputs

- **`group_col`** : group_col.
- **`real_data_path`** : real_data_path CSV DataSet.
- **`synthetic_data_path`** : synthetic_data_path CSV DataSet

### Output Values

The output is a dictionary containing the following fields:

- **`real_t_test_results`**: The real_t_test_results.
- **`synthetic_t_test_results`**: The synthetic_t_test_results.

## Examples

```python
>>> python ttest.py
>>> Loading file: ./数据/ZZZ_Sepsis_Data_From_R.csv Loading file: ./数据/YB003_DS -------------- 40 -------------- 30 -------------- 80 -------------- 100 -------------- 90 -------------- 10 -------------- 70 -------------- 50 -------------- 20 -------------- 60 Processing key: 40 Columns in DataFrame: RangeIndex(start=0, stop=600, step=1) Skipping key 40 because Demo001_Gender is not in columns Processing key: 30 Columns in DataFrame: RangeIndex(start=0, stop=450, step=1) Skipping key 30 because Demo001_Gender is not in columns Processing key: 80 Columns in DataFrame: RangeIndex(start=0, stop=1200, step=1) Skipping key 80 because Demo001_Gender is not in columns Processing key: 100 Columns in DataFrame: RangeIndex(start=0, stop=1500, step=1) Skipping key 100 because Demo001_Gender is not in columns Processing key: 90 Columns in DataFrame: RangeIndex(start=0, stop=1350, step=1) Skipping key 90 because Demo001_Gender is not in columns Processing key: 10 Columns in DataFrame: RangeIndex(start=0, stop=150, step=1) Skipping key 10 because Demo001_Gender is not in columns Processing key: 70 Columns in DataFrame: RangeIndex(start=0, stop=1050, step=1) Skipping key 70 because Demo001_Gender is not in columns Processing key: 50 Columns in DataFrame: RangeIndex(start=0, stop=750, step=1) Skipping key 50 because Demo001_Gender is not in columns Processing key: 20 Columns in DataFrame: RangeIndex(start=0, stop=300, step=1) Skipping key 20 because Demo001_Gender is not in columns Processing key: 60 Columns in DataFrame: RangeIndex(start=0, stop=900, step=1) Skipping key 60 because Demo001_Gender is not in columns Processing real_data Columns in real_data: <generator object DataFrame.items at 0x7fae0a69e2e0> t_test_result = ttest_ind(group1, group2, nan_policy='omit') Unnamed: 0 Admn001_ID Demo001_Gender Demo002_Age Demo003_ReAd Vitl001_GCS ... Flud005_Output4H Devr001_SOFA Devr002_SIRS Devr003_ShockIndex Devr004_PaFiRatio Devr005_FluidBalance 0 -4.165186 -4.194990 -inf -7.360762e+00 5.464317e+00 -4.264391 ... 1.137395e+01 2.210896 -2.251588 -2.651344 -3.864558 -1.648436 1 0.000031 0.000027 0.0 1.887744e-13 4.693368e-08 0.000020 ... 6.731314e-30 0.027052 0.024357 0.008022 0.000112 0.099276 [2 rows x 51 columns]
```
