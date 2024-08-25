| title | sdk | sdk_version | app_file | tags | description |
|-------|-----|-------------|----------|------|-------------|
|calculate_euclidean_distances| | |calculate_euclidean_distances.py|`evaluate` `metric`| |

# Metric Card for calculate_euclidean_distances

## Metric Description

The Euclidean Distance Matrix is a metric used to calculate the pairwise distances between data points in a dataset based on their numerical features. The Euclidean distance is the straight-line distance between two points in a multi-dimensional space, and it is commonly used to measure similarity or dissimilarity between data points in various applications such as clustering, dimensionality reduction, and nearest neighbor searches.

## Measurement indicators

`Continuous variables`: Euclidean distance is commonly used to measure the distance between continuous variables.

`Categorical variables`: Categorical variables generally require numerical encoding in order to be applied to Euclidean distance calculations.

## Calculation Steps

1. **Feature Selection:** The algorithm first selects all numerical features from the dataset, ensuring that only numerical data types are considered for distance computation.
2. **Distance Computation:** Using the `euclidean_distances` function from the `scikit-learn` library, the pairwise Euclidean distances between all data points in the dataset are calculated. This results in a distance matrix, where each element represents the distance between two data points.
3. **Output:** The resulting matrix, known as the Euclidean Distance Matrix, is returned. This matrix can be further used in various data analysis tasks to understand the relationships and structure within the dataset.

## How to Use

1. **Load and read data**

```python
real_data_path = "../数据/ZZZ_Sepsis_Data_From_R.csv"
synthetic_data_path = "../数据/YB003_DS"
```

2. **Create a DataMmparator object and call calculate_euclidean_distances() to get the euclidean_dist_matrix**

```python
Dc = DataComparator(real_data_path, synthetic_data_path)
euclidean_dist_matrix = Dc.calculate_euclidean_distances(df_subset)
print(euclidean_dist_matrix)
print("Euclidean Distances Calculated")
>>> [[ 0. 11436.11267685 5523.41425002 ... 32786.29385924 149033.54055248 51266.32091459] [ 11436.11267685 0. 15202.80175711 ... 43128.04830739 138355.0315513 40472.23208718] [ 5523.41425002 15202.80175711 0. ... 29286.29176064 152742.21034724 55014.65092303] ... [ 32786.29385924 43128.04830739 29286.29176064 ... 0. 181483.01270955 83600.08291104] [149033.54055248 138355.0315513 152742.21034724 ... 181483.01270955 0. 97883.03151523] [ 51266.32091459 40472.23208718 55014.65092303 ... 83600.08291104 97883.03151523 0. ]] Euclidean Distances Calculated
```

### Inputs

|input|type|desccription|
|-----|----|------------|
|df_subset|DataFrame|Dataset for inferring risk assessment|

### Output Values

The output is a dictionary containing the following fields:
|output|type|desccription|
|-----|----|------------|
|euclidean_dist_matrix|ndarray|The output matrix is a Euclidean distance matrix, where each element represents the straight-line distance between two points in the dataset. This distance matrix can help understand the similarities or differences between data points|

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
euclidean_dist_matrix = Dc.calculate_euclidean_distances(df_subset)
print(euclidean_dist_matrix)
print("Euclidean Distances Calculated")
>>> [[ 0. 11436.11267685 5523.41425002 ... 32786.29385924 149033.54055248 51266.32091459] [ 11436.11267685 0. 15202.80175711 ... 43128.04830739 138355.0315513 40472.23208718] [ 5523.41425002 15202.80175711 0. ... 29286.29176064 152742.21034724 55014.65092303] ... [ 32786.29385924 43128.04830739 29286.29176064 ... 0. 181483.01270955 83600.08291104] [149033.54055248 138355.0315513 152742.21034724 ... 181483.01270955 0. 97883.03151523] [ 51266.32091459 40472.23208718 55014.65092303 ... 83600.08291104 97883.03151523 0. ]] Euclidean Distances Calculated
```

## Limitations and Bias

The Euclidean distance is very sensitive to the scale of the data. If data in different dimensions have different scales or ranges, the Euclidean distance may be dominated by the dimension with the larger dominant scale. In this case, the distance calculation may not accurately reflect the actual similarities or differences between the data points, so data normalisation or normalisation is required.

Euclidean distances require complete data in the calculation process. If there are missing values in the dataset, it is usually not possible to calculate the Euclidean distance directly. In the case of improper handling of missing values, the distance calculation may introduce bias or cause the calculation to fail, affecting the accuracy of the analysis results.

In higher dimensional spaces, the utility of the Euclidean distance is greatly reduced. This is because as the dimensionality increases, the distances between data points tend to be similar, making it difficult to distinguish between different points. The use of Euclidean distance in high-dimensional data may lead to a degradation in the performance of clustering or classification algorithms, and therefore dimensionality reduction or the use of other distance metrics needs to be considered.

In sparse data (i.e., most of the data is zero), the computation of Euclidean distance may lead to bias because it ignores the sparsity of the data. This bias is particularly noticeable in textual data or applications in recommender systems, and can lead to incorrect similarity metrics that affect algorithm performance.

## citation

[1] Wu, X., Zhang, M., & Liu, X. (2021). "A comprehensive review of distance measures for clustering analysis in high-dimensional data." Data Science and Engineering.

[2] Mikrović, I., & Kolić, R. (2020). "Efficient algorithms for nearest neighbor search using Euclidean distance in high-dimensional spaces." Journal of Computational and Applied Mathematics.

[3] Sidiropoulos, N. D., & Ma, Y. (2020). "A survey of distance-based methods for multidimensional scaling in data visualization." IEEE Transactions on Visualization and Computer Graphics.

[4] Méndez, D., & Núñez, R. (2021). "A new approach to measuring distance in data with high dimensionality and missing values." Statistical Modelling.
