import torch
import pandas as pd
import numpy as np
from scipy.stats import f_oneway

class FTestAnalyzer:
    def __init__(self, real_data_path, synthetic_data_path):
        self.real_data = self.load_dataset(real_data_path)
        self.synthetic_data = self.load_dataset(synthetic_data_path)
        self.real_data = self.process_data(self.real_data)
        self.synthetic_data = self.process_data(self.synthetic_data)

    def load_dataset(self, file_path):
        print("Loading file:", file_path)
        if file_path.endswith('.pt') or "YB003_DS" in file_path:
            data = torch.load(file_path, map_location=torch.device('cpu'))
        elif file_path.endswith('.csv'):
            data = pd.read_csv(file_path)
        else:
            raise ValueError("Unsupported file format")
        return data

    def process_data(self, data):
        if isinstance(data, dict):
            for key in data.keys():
                data_array = np.array(data[key])
                if data_array.ndim == 3:
                    num_samples, num_features, num_times = data_array.shape
                    flattened_data = data_array.reshape(num_samples, num_features * num_times)
                elif data_array.ndim == 2:
                    flattened_data = data_array
                else:
                    raise ValueError("Unsupported data dimension")
                data[key] = pd.DataFrame(flattened_data)
        elif isinstance(data, pd.Series):
            data = pd.DataFrame(data)
        elif isinstance(data, pd.DataFrame):
            return data
        return data

    def f_test(self, df, group_col):
        f_test_results = {}
        columns = df.columns

        for col in columns:
            if df[col].dtype in ['int64', 'float64']:
                groups = [df[df[group_col] == group][col] for group in df[group_col].unique() if not df[df[group_col] == group][col].empty]
                if len(groups) > 1:
                    f_test_result = f_oneway(*groups)
                    f_test_results[col] = f_test_result
        return f_test_results

    def analyze_tests(self, group_col):
        real_f_test_results, synthetic_f_test_results = {}, {}

        if isinstance(self.synthetic_data, dict):
            for key, df in self.synthetic_data.items():
                print(f"Processing key: {key}")
                if isinstance(df, pd.DataFrame):
                    print(f"Columns in DataFrame: {df.columns}")
                    if group_col not in df.columns:
                        print(f"Skipping key {key} because {group_col} is not in columns")
                        continue
                    f_test_res = self.f_test(df, group_col)
                    synthetic_f_test_results[key] = f_test_res

        if isinstance(self.real_data, pd.DataFrame):
            print("Processing real_data")
            print(f"Columns in real_data: {self.real_data.columns}")
            real_f_test_results = self.f_test(self.real_data, group_col)

        return real_f_test_results, synthetic_f_test_results

# real_data_path ="../数据/ZZZ_Sepsis_Data_From_R.csv"
# synthetic_data_path = "../数据/YB003_DS"
# group_col = 'Demo001_Gender'
#
# analyzer = FTestAnalyzer(real_data_path, synthetic_data_path)
# real_f_test_results, synthetic_f_test_results = analyzer.analyze_tests(group_col)
#
#
# print(pd.DataFrame(real_f_test_results))