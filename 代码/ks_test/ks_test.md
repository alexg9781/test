| title | sdk | sdk_version | app_file | tags | description |
|-------|-----|-------------|----------|------|-------------|
|ks-test| | |ks_test.py|`evaluate` `metric`| |

# Metric Card for ks-test

## Metric Description

The Kolmogorov-Smirnov (KS) Test is a non-parametric test that compares the cumulative distributions of two data samples. It evaluates whether the two samples are drawn from the same distribution, providing a measure of the maximum difference between their empirical cumulative distribution functions (ECDFs).

## Calculation Steps

1. **Identifying Common Features:** The method takes two datasets (real and synthetic) as input and identifies common columns between them.
2. **Feature Selection:** For each numerical feature (with data types `int64` or `float64`), the method performs the KS test, comparing the distributions of the feature in both datasets.
3. **KS Test Calculation:** The `ks_2samp` function from the `scipy.stats` library is used to perform the KS Test. It calculates the KS statistic and p-value for each feature to assess the similarity of their distributions.
4. **Results Storage:** The results are stored in a dictionary, with feature names as keys and the KS test results (including KS statistic and p-value) as values.

## How to Use

1. **Load and read data**

```python
real_data_path = "../数据/ZZZ_Sepsis_Data_From_R.csv"
synthetic_data_path = "../数据/YB003_DS"
```

2. **Create a DataMmparator object and call ks_test() to get the ks_test_results**

```python
Dc = DataComparator(real_data_path, synthetic_data_path)
ks_test_results = Dc.ks_test()
>>> Loading file: ./数据/ZZZ_Sepsis_Data_From_R.csv Loading file: ./数据/YB003_DS Processing key: 40 Columns in DataFrame: RangeIndex(start=0, stop=600, step=1) 没有公共的列，无法执行检验 Processing key: 30 Columns in DataFrame: RangeIndex(start=0, stop=450, step=1) 没有公共的列，无法执行检验 Processing key: 80 Columns in DataFrame: RangeIndex(start=0, stop=1200, step=1) 没有公共的列，无法执行检验 Processing key: 100 Columns in DataFrame: RangeIndex(start=0, stop=1500, step=1) 没有公共的列，无法执行检验 Processing key: 90 Columns in DataFrame: RangeIndex(start=0, stop=1350, step=1) 没有公共的列，无法执行检验 Processing key: 10 Columns in DataFrame: RangeIndex(start=0, stop=150, step=1) 没有公共的列，无法执行检验 Processing key: 70 Columns in DataFrame: RangeIndex(start=0, stop=1050, step=1) 没有公共的列，无法执行检验 Processing key: 50 Columns in DataFrame: RangeIndex(start=0, stop=750, step=1) 没有公共的列，无法执行检验 Processing key: 20 Columns in DataFrame: RangeIndex(start=0, stop=300, step=1) 没有公共的列，无法执行检验 Processing key: 60 Columns in DataFrame: RangeIndex(start=0, stop=900, step=1) 没有公共的列，无法执行检验 {40: {}, 30: {}, 80: {}, 100: {}, 90: {}, 10: {}, 70: {}, 50: {}, 20: {}, 60: {}}
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
|ks_test_results|dict|Store a dictionary of KS test results between each synthetic dataset and the real dataset. The key of a dictionary is the name of the dataset, the value is another dictionary whose key is the feature name, and the value is the corresponding KS test result (including KS statistic and p-value)|

## Examples

```python
real_data_path = "../数据/ZZZ_Sepsis_Data_From_R.csv"
synthetic_data_path = "../数据/YB003_DS"
Dc = DataComparator(real_data_path, synthetic_data_path)
ks_test_results = Dc.ks_test()
print(ks_test_results)
>>> Loading file: ./数据/ZZZ_Sepsis_Data_From_R.csv Loading file: ./数据/YB003_DS Processing key: 40 Columns in DataFrame: RangeIndex(start=0, stop=600, step=1) 没有公共的列，无法执行检验 Processing key: 30 Columns in DataFrame: RangeIndex(start=0, stop=450, step=1) 没有公共的列，无法执行检验 Processing key: 80 Columns in DataFrame: RangeIndex(start=0, stop=1200, step=1) 没有公共的列，无法执行检验 Processing key: 100 Columns in DataFrame: RangeIndex(start=0, stop=1500, step=1) 没有公共的列，无法执行检验 Processing key: 90 Columns in DataFrame: RangeIndex(start=0, stop=1350, step=1) 没有公共的列，无法执行检验 Processing key: 10 Columns in DataFrame: RangeIndex(start=0, stop=150, step=1) 没有公共的列，无法执行检验 Processing key: 70 Columns in DataFrame: RangeIndex(start=0, stop=1050, step=1) 没有公共的列，无法执行检验 Processing key: 50 Columns in DataFrame: RangeIndex(start=0, stop=750, step=1) 没有公共的列，无法执行检验 Processing key: 20 Columns in DataFrame: RangeIndex(start=0, stop=300, step=1) 没有公共的列，无法执行检验 Processing key: 60 Columns in DataFrame: RangeIndex(start=0, stop=900, step=1) 没有公共的列，无法执行检验 {40: {}, 30: {}, 80: {}, 100: {}, 90: {}, 10: {}, 70: {}, 50: {}, 20: {}, 60: {}}
```

## Limitations and Bias

The K-S test is very sensitive to sample size. When the sample size is large, even very small differences in distributions may be tested as significant, while when the sample size is small, the K-S test may not have sufficient power to detect differences in distributions that actually exist. This may lead to over-rejection (i.e., over-detection of significance) in the case of large samples, or low efficacy (i.e., failure to detect significant differences that actually exist) in the case of small samples.

The K-S test is primarily used for one-dimensional data and is not applicable for multidimensional data or multivariate distributional comparisons. In cases where multidimensional data need to be analysed, the researcher needs to use other more appropriate tests, such as a multidimensional version of the K-S test or other alternative methods.

## citation

[1] Massey, F. J. Jr. (1951). "The Kolmogorov-Smirnov Test for Goodness of Fit." Journal of the American Statistical Association.

[2] Gibbons, J. D., & Chakraborti, S. (2011). "Nonparametric Statistical Inference." (5th ed.)
