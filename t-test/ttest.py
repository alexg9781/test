import torch
import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

class TTestAnalyzer:
    def __init__(self, real_data_path, synthetic_data_path):
        self.real_data = self.load_dataset(real_data_path)
        self.synthetic_data = self.load_dataset(synthetic_data_path)
        self.process_data(self.synthetic_data)

    def load_dataset(self, file_path):
        print("Loading file:", file_path)
        if file_path.endswith('.pt') or "YB003_DS" in file_path:
            data = torch.load(file_path)
        elif file_path.endswith('.csv'):
            data = pd.read_csv(file_path)
        else:
            raise ValueError("Unsupported file format")
        return data

    def process_data(self, data):
        if isinstance(data, dict):

            for key in data.keys():
                data_array = np.array(data[key])
                print("--------------", key)
                if data_array.ndim == 3:
                    num_samples, num_features, num_times = data_array.shape
                    flattened_data = data_array.reshape(num_samples, num_features * num_times)
                elif data_array.ndim == 2:
                    flattened_data = data_array
                else:
                    raise ValueError("Unsupported data dimension")
                # data是字典，key:类型 value:df
                data[key] = pd.DataFrame(flattened_data)

    def t_test(self, df, group_col):
        t_test_results = {}
        columns = df.columns

        for col in columns:
            if df[col].dtype in ['int64', 'float64']:
                if group_col in df.columns:
                    group1 = df[df[group_col] == df[group_col].unique()[0]][col]
                    group2 = df[df[group_col] == df[group_col].unique()[1]][col]
                    if not group1.empty and not group2.empty:
                        t_test_result = ttest_ind(group1, group2, nan_policy='omit')
                        t_test_results[col] = t_test_result
        return t_test_results

    def analyze_tests(self, group_col):
        real_t_test_results, synthetic_t_test_results = {}, {}

        for key, df in self.synthetic_data.items():
            print(f"Processing key: {key}")
            print(f"Columns in DataFrame: {df.columns}")
            if group_col not in df.columns:
                print(f"Skipping key {key} because {group_col} is not in columns")
                continue
            t_test_res = self.t_test(df, group_col)
            synthetic_t_test_results[key] = t_test_res

        print("Processing real_data")
        print(f"Columns in real_data: {self.real_data.items()}")
        real_t_test_results = self.t_test(self.real_data, group_col)

        return real_t_test_results, synthetic_t_test_results


real_data_path ="../数据/ZZZ_Sepsis_Data_From_R.csv"
synthetic_data_path = "../数据/YB003_DS"
group_col = 'Demo001_Gender'

analyzer = TTestAnalyzer(real_data_path, synthetic_data_path)
real_t_test_results, synthetic_t_test_results = analyzer.analyze_tests(group_col)

print(pd.DataFrame(real_t_test_results))
