| title | sdk | sdk_version | app_file | tags | description |
|-------|-----|-------------|----------|------|-------------|
|correlation| | |correlation.py|`evaluate` `metric`| |

# Metric Card for correlation

## Metric Description

Correlation Analysis is a method used to measure the strength and direction of the relationship between pairs of numerical features in a dataset. The primary metrics used in this analysis are Pearson's correlation coefficient and Spearman's rank correlation coefficient.

## Measurement indicators

### Pearson correlation coefficient

`Continuous variable`: Pearson correlation coefficient is used to measure the linear relationship between two continuous variables.

`Categorical variable`: Pearson correlation coefficient is not applicable to categorical variables. If categorical variables need to be processed, they can be converted into binary variables (such as 0 and 1) for calculation, but this is not a standard usage method.

### Spearman correlation coefficient

`Continuous variables`: Spearman correlation coefficient can be used for continuous variables, but it does not require the relationship between variables to be linear, but rather based on rank correlation.

`Categorical variables`: applicable to ordinal variables (categorical variables that can be arranged in order). For nominal categorical variables, it is usually necessary to convert them into binary variables to calculate correlation.

## Calculation Steps

1. **Feature Pairing:** All pairs of numerical features (columns with data types `int64` or `float64`) in the dataset are identified for correlation analysis.
2. **Pearson's Correlation Coefficient (`pearsonr`):** This metric is computed for each pair of features to measure their linear relationship. The result ranges from -1 to 1, where 1 indicates a perfect positive linear relationship, -1 indicates a perfect negative linear relationship, and 0 indicates no linear relationship.
3. **Spearman's Rank Correlation Coefficient (`spearmanr`):** This metric is computed for each pair of features to measure their monotonic relationship. It is suitable for assessing both linear and non-linear correlations and also ranges from -1 to 1.
4. **Missing Value Handling:** Any missing values in the dataset are filled with zeros to ensure the correlation calculations are not disrupted.
5. **Results Storage:** The calculated Pearson and Spearman correlation coefficients for each feature pair are stored in two dictionaries, one for Pearson and one for Spearman correlations.

## Interpretation

- **Pearson's Correlation Coefficient:** A value close to 1 or -1 indicates a strong linear relationship between the two features, while a value close to 0 indicates little to no linear relationship.
- **Spearman's Rank Correlation Coefficient:** A value close to 1 or -1 indicates a strong monotonic relationship, whether it is linear or non-linear, between the two features. A value close to 0 suggests that the features do not have a consistent monotonic relationship.
- **Use Cases:** This analysis helps in identifying relationships between features, which can be used for feature selection, multicollinearity diagnosis, and understanding underlying data patterns.

## How to Use

1. **Load and read data**

```python
real_data_path = "../数据/ZZZ_Sepsis_Data_From_R.csv"
synthetic_data_path = "../数据/YB003_DS"
```

2. **Create a DataMmparator object and call correlation() to get the pearson_results, spearman_results**

```python
Dc = DataComparator(real_data_path, synthetic_data_path)
pearson_results, spearman_results = Dc.correlation()
print(euclidean_dist_matrix)
>>> Loading file: ./运行版/数据/ZZZ_Sepsis_Data_From_R.csv Loading file: ./运行版/数据/YB003_DS Processing key: 40 Columns in DataFrame: RangeIndex(start=0, stop=600, step=1) 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 600/600 [08:57<00:00, 1.12it/s] Processing key: 30 Columns in DataFrame: RangeIndex(start=0, stop=450, step=1) 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 450/450 [05:12<00:00, 1.44it/s] Processing key: 80 Columns in DataFrame: RangeIndex(start=0, stop=1200, step=1) 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1200/1200 [34:31<00:00, 1.73s/it] Processing key: 100 ...
```

### Inputs

|input|type|desccription|
|-----|----|------------|
|real_data_path|str|The file path of a real dataset, usually a string containing the path to the CSV file or other format data file to be loaded|
|synthetic_data_path|str|The file path of the synthetic dataset, similar to the path of a real dataset, represents the storage location of the synthetic data|

### Output Values

The output is a dictionary containing the following fields:

|output|type|desccription|
|-----|----|------------|
|pearson_results|dict|A dictionary that stores Pearson correlation coefficients for all feature pairs. The keys of a dictionary are feature pairs (represented in tuple form), and the values are the corresponding Pearson correlation coefficients and their p-values|
|spearman_results|dict|A dictionary that stores Spearman correlation coefficients for all feature pairs. The keys of a dictionary are also feature pairs (represented in tuple form), and the values are the corresponding Spearman correlation coefficients and their p-values|

## Examples

```python
real_data_path = "../数据/ZZZ_Sepsis_Data_From_R.csv"
synthetic_data_path = "../数据/YB003_DS"
Dc = DataComparator(real_data_path, synthetic_data_path)
pearson_results, spearman_results = Dc.correlation()
# 第一个值：相关系数 第二个值：p值
print(pd.DataFrame(pearson_results))
>>> Loading file: ./运行版/数据/ZZZ_Sepsis_Data_From_R.csv Loading file: ./运行版/数据/YB003_DS Processing key: 40 Columns in DataFrame: RangeIndex(start=0, stop=600, step=1) 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 600/600 [08:57<00:00, 1.12it/s] Processing key: 30 Columns in DataFrame: RangeIndex(start=0, stop=450, step=1) 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 450/450 [05:12<00:00, 1.44it/s] Processing key: 80 Columns in DataFrame: RangeIndex(start=0, stop=1200, step=1) 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1200/1200 [34:31<00:00, 1.73s/it] Processing key: 100 ...
```

## Limitations and Bias

Pearson correlation coefficients assume that data follow a normal distribution, especially when used to infer statistical significance. If the data are not normally distributed, the results of the Pearson correlation coefficient may be inaccurate. In data that is not normally distributed, the Pearson correlation coefficient may not accurately reflect the actual relationship between the variables.

Spearman correlation coefficients are calculated based on the rank of the data and are therefore sensitive to the accuracy of the rank calculation. Especially when there are a large number of repeated values, the rank may not accurately reflect the actual relationship in the data. When there are a large number of duplicate values in the data, the calculation of Spearman's correlation coefficient may be inaccurate, resulting in biased results.

## citation

[1] Wu, H., & Wang, S. (2020). "A Comparative Study of Pearson’s and Spearman’s Correlation Coefficients in Transcriptome Data Analysis." Journal of Computational Biology.

[2] Schober, P., Boer, C., & Schwarte, L. A. (2018). "Correlation coefficients: appropriate use and interpretation." Anesthesia & Analgesia.
