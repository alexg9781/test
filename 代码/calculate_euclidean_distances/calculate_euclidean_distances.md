| title | sdk | sdk_version | app_file | tags | description |
|-------|-----|-------------|----------|------|-------------|
|calculate_euclidean_distances| | |calculate_euclidean_distances.py|`evaluate` `metric`| |

# Metric Card for calculate_euclidean_distances

## Metric Description

See the [calculate_euclidean_distances README.md](https://github.com/khloe-S/test/tree/main/calculate_euclidean_distances) for more information.

## How to Use

1. **Install the related packages**

```python
pip install -r requirements.txt
```

2. **To run the calculate_euclidean_distances.py file or enter the following code in the terminal:**

```python
python calculate_euclidean_distances.py
```

```python
euclidean_dist_matrix = calculate_euclidean_distances(df_subset)
print(euclidean_dist_matrix)
print("Euclidean Distances Calculated")
>>> [[ 0. 11436.11267685 5523.41425002 ... 32786.29385924 149033.54055248 51266.32091459] [ 11436.11267685 0. 15202.80175711 ... 43128.04830739 138355.0315513 40472.23208718] [ 5523.41425002 15202.80175711 0. ... 29286.29176064 152742.21034724 55014.65092303] ... [ 32786.29385924 43128.04830739 29286.29176064 ... 0. 181483.01270955 83600.08291104] [149033.54055248 138355.0315513 152742.21034724 ... 181483.01270955 0. 97883.03151523] [ 51266.32091459 40472.23208718 55014.65092303 ... 83600.08291104 97883.03151523 0. ]] Euclidean Distances Calculated
```

### Inputs

- **`df_subset`** : CSV DataSet

### Output Values

The output is a dictionary containing the following fields:

- **`euclidean_dist_matrix`**: The Euclidean Distances Calculated

## Examples

```python
>>> python calculate_euclidean_distances.py
>>> [[ 0. 11436.11267685 5523.41425002 ... 32786.29385924 149033.54055248 51266.32091459] [ 11436.11267685 0. 15202.80175711 ... 43128.04830739 138355.0315513 40472.23208718] [ 5523.41425002 15202.80175711 0. ... 29286.29176064 152742.21034724 55014.65092303] ... [ 32786.29385924 43128.04830739 29286.29176064 ... 0. 181483.01270955 83600.08291104] [149033.54055248 138355.0315513 152742.21034724 ... 181483.01270955 0. 97883.03151523] [ 51266.32091459 40472.23208718 55014.65092303 ... 83600.08291104 97883.03151523 0. ]] Euclidean Distances Calculated
```
