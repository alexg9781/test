import torch
import pandas as pd
import numpy as np
from scipy.stats import pearsonr, spearmanr
from tqdm import tqdm

class CorrelationAnalyzer:
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
            print("执行 series to df")
            data = pd.DataFrame(data)
        return data

    def correlation_tests(self, df):
        pearson_results = {}
        spearman_results = {}
        columns = df.columns
        for col1 in tqdm(columns):
            for col2 in columns:
                if col1 != col2 and df[col1].dtype in ['int64', 'float64'] and df[col2].dtype in ['int64', 'float64']:
                    pearson_result = pearsonr(df[col1].fillna(0), df[col2].fillna(0))
                    spearman_result = spearmanr(df[col1].fillna(0), df[col2].fillna(0))
                    pearson_results[(col1, col2)] = pearson_result
                    spearman_results[(col1, col2)] = spearman_result
        return pearson_results, spearman_results

    def analyze_tests(self):
        pearson_results = {}
        spearman_results = {}

        if isinstance(self.synthetic_data, dict):
            for key, df in self.synthetic_data.items():
                print(f"Processing key: {key}")
                if isinstance(df, pd.DataFrame):
                    print(f"Columns in DataFrame: {df.columns}")
                    pearson_res, spearman_res = self.correlation_tests(df)
                    pearson_results[key] = pearson_res
                    spearman_results[key] = spearman_res

        if isinstance(self.real_data, pd.DataFrame):
            real_pearson_res, real_spearman_res = self.correlation_tests(self.real_data)
            pearson_results['real_data'] = real_pearson_res
            spearman_results['real_data'] = real_spearman_res

        return pearson_results, spearman_results

real_data_path ="../数据/ZZZ_Sepsis_Data_From_R.csv"
synthetic_data_path = "../数据/YB003_DS"

analyzer = CorrelationAnalyzer(real_data_path, synthetic_data_path)
pearson_results, spearman_results = analyzer.analyze_tests()
# 第一个值：相关系数 第二个值：p值
print(pd.DataFrame(pearson_results))
