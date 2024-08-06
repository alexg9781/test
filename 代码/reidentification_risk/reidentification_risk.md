| title | sdk | sdk_version | app_file | tags | description |
|-------|-----|-------------|----------|------|-------------|
|reidentification_risk| | |reidentification_risk.py|`evaluate` `metric`| |

# Metric Card for reidentification_risk

## Metric Description

See the [reidentification_risk README.md](https://github.com/khloe-S/test/tree/main/reidentification_risk) for more information.

## How to Use

1. **Install the related packages**

```python
pip install -r requirements.txt
```

2. **To run the reidentification_risk.py file or enter the following code in the terminal:**

```python
python reidentification_risk.py
```

```python
>>> unique_identifier = 'PatientID'
>>> reidentification_risk_value = reidentification_risk(df_combined, unique_identifier)
>>> print(f"Re-identification Risk: {reidentification_risk_value}")
>>> Re-identification Risk: 0.99
```

### Inputs

- **`unique_identifier`** : Example attribute.
- **`df_combined`** : CSV DataSet

### Output Values

The output is a dictionary containing the following fields:

- **`reidentification_risk_value`**: The Re-identification Risk.

## Examples

```python
>>> python reidentification_risk.py
>>> Re-identification Risk: 0.99
```
