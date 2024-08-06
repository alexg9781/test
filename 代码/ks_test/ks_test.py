import torch
import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

class KSTestAnalyzer:
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
                if data_array.ndim == 3:
                    num_samples, num_features, num_times = data_array.shape
                    flattened_data = data_array.reshape(num_samples, num_features * num_times)
                elif data_array.ndim == 2:
                    flattened_data = data_array
                else:
                    raise ValueError("Unsupported data dimension")
                data[key] = pd.DataFrame(flattened_data)

    def ks_test(self, df1, df2):
        ks_test_results = {}
        common_columns = [col for col in df1.columns if col in df2.columns]
        if not common_columns:
            print("没有公共的列，无法执行检验")
        else:
            print("有共同的列，可以执行检验")
            for col in common_columns:
                if df1[col].dtype in ['int64', 'float64'] and df2[col].dtype in ['int64', 'float64']:
                    ks_test_result = ks_2samp(df1[col].dropna(), df2[col].dropna())
                    ks_test_results[col] = ks_test_result
        return ks_test_results

    def analyze_tests(self):
        ks_test_results = {}

        for key, df in self.synthetic_data.items():
            print(f"Processing key: {key}")
            print(f"Columns in DataFrame: {df.columns}")
            ks_test_res = self.ks_test(self.real_data, df)
            ks_test_results[key] = ks_test_res

        return ks_test_results
#
# real_data_path ="../数据/ZZZ_Sepsis_Data_From_R.csv"
# synthetic_data_path = "../数据/YB003_DS"
#
# analyzer = KSTestAnalyzer(real_data_path, synthetic_data_path)
# ks_test_results = analyzer.analyze_tests()
# print(ks_test_results)