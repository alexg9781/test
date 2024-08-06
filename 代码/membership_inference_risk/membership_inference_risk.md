| title | sdk | sdk_version | app_file | tags | description |
|-------|-----|-------------|----------|------|-------------|
|membership_inference_risk| | |membership_inference_risk.py|`evaluate` `metric`| |

# Metric Card for membership_inference_risk

## Metric Description

See the [membership_inference_risk README.md](https://github.com/khloe-S/test/tree/main/membership_inference_risk) for more information.

## How to Use

1. **Install the related packages**

```python
pip install -r requirements.txt
```

2. **To run the membership_inference_risk.py file or enter the following code in the terminal:**

```python
python membership_inference_risk.py
```

```python
>>> membership_risk = membership_inference_risk(df_combined)
>>> print(f"Membership Inference Risk: {membership_risk}")
>>> Membership Inference Risk: 0.99
```

### Inputs

- **`df_combined`** : CSV DataSet

### Output Values

The output is a dictionary containing the following fields:

- **`membership_risk`**: The Membership Inference Risk.

## Examples

```python
>>> python membership_inference_risk.py
>>> Membership Inference Risk: 0.99
```
