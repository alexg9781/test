| title | sdk | sdk_version | app_file | tags | description |
|-------|-----|-------------|----------|------|-------------|
|ks-test| | |ks_test.py|`evaluate` `metric`| |

# Metric Card for ks-test

## Metric Description

See the [ks-test README.md](https://github.com/khloe-S/test/tree/main/ks-test) for more information.

## How to Use

1. **Install the related packages**

```python
pip install -r requirements.txt
```

2. **To run the ks_test.py file or enter the following code in the terminal:**

```python
python ks_test.py
```

```python
>>> real_data_path ="../数据/ZZZ_Sepsis_Data_From_R.csv"
>>> synthetic_data_path = "../数据/YB003_DS"
>>> analyzer = KSTestAnalyzer(real_data_path, synthetic_data_path)
>>> ks_test_results = analyzer.analyze_tests()
>>> print(ks_test_results)
>>> Loading file: ./数据/ZZZ_Sepsis_Data_From_R.csv Loading file: ./数据/YB003_DS Processing key: 40 Columns in DataFrame: RangeIndex(start=0, stop=600, step=1) 没有公共的列，无法执行检验 Processing key: 30 Columns in DataFrame: RangeIndex(start=0, stop=450, step=1) 没有公共的列，无法执行检验 Processing key: 80 Columns in DataFrame: RangeIndex(start=0, stop=1200, step=1) 没有公共的列，无法执行检验 Processing key: 100 Columns in DataFrame: RangeIndex(start=0, stop=1500, step=1) 没有公共的列，无法执行检验 Processing key: 90 Columns in DataFrame: RangeIndex(start=0, stop=1350, step=1) 没有公共的列，无法执行检验 Processing key: 10 Columns in DataFrame: RangeIndex(start=0, stop=150, step=1) 没有公共的列，无法执行检验 Processing key: 70 Columns in DataFrame: RangeIndex(start=0, stop=1050, step=1) 没有公共的列，无法执行检验 Processing key: 50 Columns in DataFrame: RangeIndex(start=0, stop=750, step=1) 没有公共的列，无法执行检验 Processing key: 20 Columns in DataFrame: RangeIndex(start=0, stop=300, step=1) 没有公共的列，无法执行检验 Processing key: 60 Columns in DataFrame: RangeIndex(start=0, stop=900, step=1) 没有公共的列，无法执行检验 {40: {}, 30: {}, 80: {}, 100: {}, 90: {}, 10: {}, 70: {}, 50: {}, 20: {}, 60: {}}
```

### Inputs

- **`real_data_path`** : real_data_path CSV DataSet.
- **`synthetic_data_path`** : synthetic_data_path CSV DataSet

### Output Values

The output is a dictionary containing the following fields:

- **`ks_test_results`**: The ks_test_results.

## Examples

```python
>>> python ks_test.py
>>> Loading file: ./数据/ZZZ_Sepsis_Data_From_R.csv Loading file: ./数据/YB003_DS Processing key: 40 Columns in DataFrame: RangeIndex(start=0, stop=600, step=1) 没有公共的列，无法执行检验 Processing key: 30 Columns in DataFrame: RangeIndex(start=0, stop=450, step=1) 没有公共的列，无法执行检验 Processing key: 80 Columns in DataFrame: RangeIndex(start=0, stop=1200, step=1) 没有公共的列，无法执行检验 Processing key: 100 Columns in DataFrame: RangeIndex(start=0, stop=1500, step=1) 没有公共的列，无法执行检验 Processing key: 90 Columns in DataFrame: RangeIndex(start=0, stop=1350, step=1) 没有公共的列，无法执行检验 Processing key: 10 Columns in DataFrame: RangeIndex(start=0, stop=150, step=1) 没有公共的列，无法执行检验 Processing key: 70 Columns in DataFrame: RangeIndex(start=0, stop=1050, step=1) 没有公共的列，无法执行检验 Processing key: 50 Columns in DataFrame: RangeIndex(start=0, stop=750, step=1) 没有公共的列，无法执行检验 Processing key: 20 Columns in DataFrame: RangeIndex(start=0, stop=300, step=1) 没有公共的列，无法执行检验 Processing key: 60 Columns in DataFrame: RangeIndex(start=0, stop=900, step=1) 没有公共的列，无法执行检验 {40: {}, 30: {}, 80: {}, 100: {}, 90: {}, 10: {}, 70: {}, 50: {}, 20: {}, 60: {}}
```
