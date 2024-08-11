| title | sdk | sdk_version | app_file | tags | description |
|-------|-----|-------------|----------|------|-------------|
|f-test| | |ftest.py|`evaluate` `metric`| |

# Metric Card for ftest

## Metric Description

The F-Test (Analysis of Variance, ANOVA) is a statistical method used to compare the means of multiple groups to determine if there are any statistically significant differences between them. It helps in identifying whether the variation in the data is due to the group classification or due to random chance.

## Calculation Steps

1. **Grouping Data:** The method takes a dataset and a grouping column as input. It groups the data based on the unique values of the grouping column.
2. **Feature Selection:** For each numerical feature (with data types `int64` or `float64`), the method retrieves the corresponding values from each group.
3. **F-Test Calculation:** The `f_oneway` function from the `scipy.stats` library is used to perform the F-Test. It calculates the F-statistic and p-value for each feature to assess the significance of the differences in means across groups.
4. **Results Storage:** The results are stored in a dictionary, with the feature names as keys and the F-test results (including F-statistic and p-value) as values.

## How to Use

1. **Load and read data**

```python
real_data_path = "../数据/ZZZ_Sepsis_Data_From_R.csv"
synthetic_data_path = "../数据/YB003_DS"
```

2. **Create a DataMmparator object and call ftest() to get the real_f_test_results, synthetic_f_test_results**

```python
Dc = DataComparator(real_data_path, synthetic_data_path)
group_col = 'Demo001_Gender'
real_f_test_results, synthetic_f_test_results = Dc.ftest(group_col)
print(pd.DataFrame(real_f_test_results))
>>> Loading file: ./数据/ZZZ_Sepsis_Data_From_R.csv Loading file: ./数据/ZZZ_Sepsis_Data_From_R.csv Processing real_data Columns in real_data: Index(['Unnamed: 0', 'Admn001_ID', 'Demo001_Gender', 'Demo002_Age', 'Demo003_ReAd', 'Vitl001_GCS', 'Vitl002_HR', 'Vitl003_SysBP', 'Vitl004_MeanBP', 'Vitl005_DiaBP', 'Vitl006_RR', 'Vitl007_SpO2', 'Vitl008_Temp', 'Labs001_K', 'Labs002_Na', 'Labs003_Cl', 'Labs004_Glucose', 'Labs005_BUN', 'Labs006_Creatinine', 'Labs007_Mg', 'Labs008_Ca', 'Labs009_IonisedCa', 'Labs010_CO2', 'Labs011_SGOT', 'Labs012_SGPT', 'Labs013_TotalBili', 'Labs014_Albumin', 'Labs015_Hb', 'Labs016_WbcCount', 'Labs017_PlateletsCount', 'Labs018_PTT', 'Labs019_PT', 'Labs020_INR', 'Labs021_pH', 'Labs022_PaO2', 'Labs023_PaCO2', 'Labs024_BE', 'Labs025_HCO3', 'Labs026_Lactate', 'Vent001_Mech', 'Vent002_FiO2', 'Flud001_InputTotal', 'Flud002_Input4H', 'Flud003_MaxVaso', 'Flud004_OutputTotal', 'Flud005_Output4H', 'Devr001_SOFA', 'Devr002_SIRS', 'Devr003_ShockIndex', 'Devr004_PaFiRatio', 'Devr005_FluidBalance'], dtype='object') Unnamed: 0 Admn001_ID Demo001_Gender Demo002_Age Demo003_ReAd ... Devr001_SOFA Devr002_SIRS Devr003_ShockIndex Devr004_PaFiRatio Devr005_FluidBalance 0 17.348774 17.597944 inf 5.418081e+01 2.985876e+01 ... 4.888063 5.069649 7.029627 14.934811 2.717342 1 0.000031 0.000027 0.0 1.887744e-13 4.693368e-08 ... 0.027052 0.024357 0.008022 0.000112 0.099276
```

### Inputs

|input|type|desccription|
|-----|----|------------|
|real_data_path|str|The file path of a real dataset, usually a string containing the path to the CSV file or other format data file to be loaded|
|synthetic_data_path|str|The file path of the synthetic dataset, similar to the path of a real dataset, represents the storage location of the synthetic data|
|group_col|str|The name of the data column used for grouping. This column contains categorical data, which is divided into multiple groups based on its unique value to perform F-tests on numerical features|

### Output Values

The output is a dictionary containing the following fields:

|output|type|desccription|
|-----|----|------------|
|real_f_test_results|dict|A dictionary that stores F-test results for all numerical features in a real dataset. The key of the dictionary is the feature name, and the value is the corresponding F-test result (including F-statistic and p-value)|
|synthetic_f_test_results|dict|A dictionary that stores the F-test results of all numerical features in a synthetic dataset. The key of a dictionary is the name of the dataset, the value is another dictionary whose key is the feature name, and the value is the corresponding F-test result (including F-statistic and p-value)|

## Examples

```python
real_data_path = "../数据/ZZZ_Sepsis_Data_From_R.csv"
synthetic_data_path = "../数据/YB003_DS"
Dc = DataComparator(real_data_path, synthetic_data_path)
group_col = 'Demo001_Gender'
real_f_test_results, synthetic_f_test_results = Dc.ftest(group_col)
print(pd.DataFrame(real_f_test_results))
>>> Loading file: ./数据/ZZZ_Sepsis_Data_From_R.csv Loading file: ./数据/ZZZ_Sepsis_Data_From_R.csv Processing real_data Columns in real_data: Index(['Unnamed: 0', 'Admn001_ID', 'Demo001_Gender', 'Demo002_Age', 'Demo003_ReAd', 'Vitl001_GCS', 'Vitl002_HR', 'Vitl003_SysBP', 'Vitl004_MeanBP', 'Vitl005_DiaBP', 'Vitl006_RR', 'Vitl007_SpO2', 'Vitl008_Temp', 'Labs001_K', 'Labs002_Na', 'Labs003_Cl', 'Labs004_Glucose', 'Labs005_BUN', 'Labs006_Creatinine', 'Labs007_Mg', 'Labs008_Ca', 'Labs009_IonisedCa', 'Labs010_CO2', 'Labs011_SGOT', 'Labs012_SGPT', 'Labs013_TotalBili', 'Labs014_Albumin', 'Labs015_Hb', 'Labs016_WbcCount', 'Labs017_PlateletsCount', 'Labs018_PTT', 'Labs019_PT', 'Labs020_INR', 'Labs021_pH', 'Labs022_PaO2', 'Labs023_PaCO2', 'Labs024_BE', 'Labs025_HCO3', 'Labs026_Lactate', 'Vent001_Mech', 'Vent002_FiO2', 'Flud001_InputTotal', 'Flud002_Input4H', 'Flud003_MaxVaso', 'Flud004_OutputTotal', 'Flud005_Output4H', 'Devr001_SOFA', 'Devr002_SIRS', 'Devr003_ShockIndex', 'Devr004_PaFiRatio', 'Devr005_FluidBalance'], dtype='object') Unnamed: 0 Admn001_ID Demo001_Gender Demo002_Age Demo003_ReAd ... Devr001_SOFA Devr002_SIRS Devr003_ShockIndex Devr004_PaFiRatio Devr005_FluidBalance 0 17.348774 17.597944 inf 5.418081e+01 2.985876e+01 ... 4.888063 5.069649 7.029627 14.934811 2.717342 1 0.000031 0.000027 0.0 1.887744e-13 4.693368e-08 ... 0.027052 0.024357 0.008022 0.000112 0.099276
```

## Limitations and Bias

The F-test is very sensitive to outliers. Outliers may significantly affect the within-group variance and between-group variance, thus affecting the statistics of the F-test. Outliers may lead to excessively significant results, even if the differences are not significant.

When multiple F-tests are performed on the same dataset, the probability of a Type I error accumulates. This increases the risk of detecting spurious significant differences. The cumulative error rate resulting from the multiple comparison problem makes the results less reliable, and it may be necessary to adjust the significance level or use other methods to control the error rate.

## citation

[1] Gelman, A., Hill, J., & Vehtari, A. (2020). "Regression and Other Stories." Cambridge University Press.

[2] Shieh, G. (2020). "Exact power and sample size calculations for the two-sample F-test." Journal of Statistical Computation and Simulation.
