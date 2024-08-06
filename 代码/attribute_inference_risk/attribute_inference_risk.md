| title | sdk | sdk_version | app_file | tags | description |
|-------|-----|-------------|----------|------|-------------|
|attribute_inference_risk| | |attribute_inference_risk.py|`evaluate` `metric`| |

# Metric Card for attribute_inference_risk

## Metric Description

See the [attribute_inference_risk README.md](https://github.com/khloe-S/test/tree/main/attribute_inference_risk) for more information.

## How to Use

1. **Install the related packages**

```python
pip install -r requirements.txt
```

2. **To run the ks_test.py file or enter the following code in the terminal:**

```python
python attribute_inference_risk.py
```

```python
attribute = 'Age'  # Example attribute
if attribute in df_combined.columns:
    attribute_risk = attribute_inference_risk(df_combined, attribute)
    print(f"Attribute Inference Risk for {attribute}: {attribute_risk}")
else:
    print(f"Attribute {attribute} not found in the data")
>>> Attribute Inference Risk for Age: 0.19999999999999996
```

### Inputs

- **`attribute`** : Example attribute.
- **`df_combined`** : CSV DataSet

### Output Values

The output is a dictionary containing the following fields:

- **`Attribute`**: The Attribute Inference Risk for Age.

## Examples

```python
>>> python attribute_inference_risk.py
>>> Attribute Inference Risk for Age: 0.19999999999999996
```
