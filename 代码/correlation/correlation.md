| title | sdk | sdk_version | app_file | tags | description |
|-------|-----|-------------|----------|------|-------------|
|correlation| | |correlation.py|`evaluate` `metric`| |

# Metric Card for correlation

## Metric Description

See the [correlation README.md](https://github.com/khloe-S/test/tree/main/correlation) for more information.

## How to Use

1. **Install the related packages**

```python
pip install -r requirements.txt
```

2. **To run the correlation.py file or enter the following code in the terminal:**

```python
python correlation.py
```

```python
>>> real_data_path ="../数据/ZZZ_Sepsis_Data_From_R.csv"
>>> synthetic_data_path = "../数据/YB003_DS"
>>> analyzer = CorrelationAnalyzer(real_data_path, synthetic_data_path)
>>> pearson_results, spearman_results = analyzer.analyze_tests()
>>> # 第一个值：相关系数 第二个值：p值
>>> print(pd.DataFrame(pearson_results))
>>> Loading file: ./运行版/数据/ZZZ_Sepsis_Data_From_R.csv Loading file: ./运行版/数据/YB003_DS Processing key: 40 Columns in DataFrame: RangeIndex(start=0, stop=600, step=1) 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 600/600 [08:57<00:00, 1.12it/s] Processing key: 30 Columns in DataFrame: RangeIndex(start=0, stop=450, step=1) 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 450/450 [05:12<00:00, 1.44it/s] Processing key: 80 Columns in DataFrame: RangeIndex(start=0, stop=1200, step=1) 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1200/1200 [34:31<00:00, 1.73s/it] Processing key: 100 ...
```

### Inputs

- **`real_data_path`** : real_data_path CSV DataSet.
- **`synthetic_data_path`** : synthetic_data_path CSV DataSet

### Output Values

The output is a dictionary containing the following fields:

- **`pearson_results`**: The Apearson_results.
- **`spearman_results`**: The spearman_results.

## Examples

```python
>>> python correlation.py
>>> Loading file: ./运行版/数据/ZZZ_Sepsis_Data_From_R.csv Loading file: ./运行版/数据/YB003_DS Processing key: 40 Columns in DataFrame: RangeIndex(start=0, stop=600, step=1) 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 600/600 [08:57<00:00, 1.12it/s] Processing key: 30 Columns in DataFrame: RangeIndex(start=0, stop=450, step=1) 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 450/450 [05:12<00:00, 1.44it/s] Processing key: 80 Columns in DataFrame: RangeIndex(start=0, stop=1200, step=1) 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1200/1200 [34:31<00:00, 1.73s/it] Processing key: 100 ...
```
