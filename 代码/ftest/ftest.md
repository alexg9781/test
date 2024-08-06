| title | sdk | sdk_version | app_file | tags | description |
|-------|-----|-------------|----------|------|-------------|
|f-test| | |ftest.py|`evaluate` `metric`| |

# Metric Card for ftest

## Metric Description

See the [ftest README.md](https://github.com/khloe-S/test/tree/main/f-test) for more information.

## How to Use

1. **Install the related packages**

```python
pip install -r requirements.txt
```

2. **To run the ftest.py file or enter the following code in the terminal:**

```python
python ftest.py
```

```python
>>> real_data_path ="../数据/ZZZ_Sepsis_Data_From_R.csv"
>>> synthetic_data_path = "../数据/YB003_DS"
>>> group_col = 'Demo001_Gender'
>>> analyzer = FTestAnalyzer(real_data_path, synthetic_data_path)
>>> real_f_test_results, synthetic_f_test_results = analyzer.analyze_tests(group_col)
>>> print(pd.DataFrame(real_f_test_results))

>>> Loading file: ./数据/ZZZ_Sepsis_Data_From_R.csv Loading file: ./数据/ZZZ_Sepsis_Data_From_R.csv Processing real_data Columns in real_data: Index(['Unnamed: 0', 'Admn001_ID', 'Demo001_Gender', 'Demo002_Age', 'Demo003_ReAd', 'Vitl001_GCS', 'Vitl002_HR', 'Vitl003_SysBP', 'Vitl004_MeanBP', 'Vitl005_DiaBP', 'Vitl006_RR', 'Vitl007_SpO2', 'Vitl008_Temp', 'Labs001_K', 'Labs002_Na', 'Labs003_Cl', 'Labs004_Glucose', 'Labs005_BUN', 'Labs006_Creatinine', 'Labs007_Mg', 'Labs008_Ca', 'Labs009_IonisedCa', 'Labs010_CO2', 'Labs011_SGOT', 'Labs012_SGPT', 'Labs013_TotalBili', 'Labs014_Albumin', 'Labs015_Hb', 'Labs016_WbcCount', 'Labs017_PlateletsCount', 'Labs018_PTT', 'Labs019_PT', 'Labs020_INR', 'Labs021_pH', 'Labs022_PaO2', 'Labs023_PaCO2', 'Labs024_BE', 'Labs025_HCO3', 'Labs026_Lactate', 'Vent001_Mech', 'Vent002_FiO2', 'Flud001_InputTotal', 'Flud002_Input4H', 'Flud003_MaxVaso', 'Flud004_OutputTotal', 'Flud005_Output4H', 'Devr001_SOFA', 'Devr002_SIRS', 'Devr003_ShockIndex', 'Devr004_PaFiRatio', 'Devr005_FluidBalance'], dtype='object') Unnamed: 0 Admn001_ID Demo001_Gender Demo002_Age Demo003_ReAd ... Devr001_SOFA Devr002_SIRS Devr003_ShockIndex Devr004_PaFiRatio Devr005_FluidBalance 0 17.348774 17.597944 inf 5.418081e+01 2.985876e+01 ... 4.888063 5.069649 7.029627 14.934811 2.717342 1 0.000031 0.000027 0.0 1.887744e-13 4.693368e-08 ... 0.027052 0.024357 0.008022 0.000112 0.099276
```

### Inputs

- **`real_data_path`** : real_data_path CSV DataSet.
- **`synthetic_data_path`** : synthetic_data_path CSV DataSet
- **`group_col`** : group_col

### Output Values

The output is a dictionary containing the following fields:

- **`real_f_test_results`**: The real_f_test_results.
- **`synthetic_f_test_results`**: The synthetic_f_test_results.

## Examples

```python
>>> python ftest.py
>>> Loading file: ./数据/ZZZ_Sepsis_Data_From_R.csv Loading file: ./数据/ZZZ_Sepsis_Data_From_R.csv Processing real_data Columns in real_data: Index(['Unnamed: 0', 'Admn001_ID', 'Demo001_Gender', 'Demo002_Age', 'Demo003_ReAd', 'Vitl001_GCS', 'Vitl002_HR', 'Vitl003_SysBP', 'Vitl004_MeanBP', 'Vitl005_DiaBP', 'Vitl006_RR', 'Vitl007_SpO2', 'Vitl008_Temp', 'Labs001_K', 'Labs002_Na', 'Labs003_Cl', 'Labs004_Glucose', 'Labs005_BUN', 'Labs006_Creatinine', 'Labs007_Mg', 'Labs008_Ca', 'Labs009_IonisedCa', 'Labs010_CO2', 'Labs011_SGOT', 'Labs012_SGPT', 'Labs013_TotalBili', 'Labs014_Albumin', 'Labs015_Hb', 'Labs016_WbcCount', 'Labs017_PlateletsCount', 'Labs018_PTT', 'Labs019_PT', 'Labs020_INR', 'Labs021_pH', 'Labs022_PaO2', 'Labs023_PaCO2', 'Labs024_BE', 'Labs025_HCO3', 'Labs026_Lactate', 'Vent001_Mech', 'Vent002_FiO2', 'Flud001_InputTotal', 'Flud002_Input4H', 'Flud003_MaxVaso', 'Flud004_OutputTotal', 'Flud005_Output4H', 'Devr001_SOFA', 'Devr002_SIRS', 'Devr003_ShockIndex', 'Devr004_PaFiRatio', 'Devr005_FluidBalance'], dtype='object') Unnamed: 0 Admn001_ID Demo001_Gender Demo002_Age Demo003_ReAd ... Devr001_SOFA Devr002_SIRS Devr003_ShockIndex Devr004_PaFiRatio Devr005_FluidBalance 0 17.348774 17.597944 inf 5.418081e+01 2.985876e+01 ... 4.888063 5.069649 7.029627 14.934811 2.717342 1 0.000031 0.000027 0.0 1.887744e-13 4.693368e-08 ... 0.027052 0.024357 0.008022 0.000112 0.099276
```
