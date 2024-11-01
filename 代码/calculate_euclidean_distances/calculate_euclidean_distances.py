import numpy as np
from sklearn.metrics.pairwise import euclidean_distances

# 计算欧几里得距离
# def calculate_euclidean_distances(df):
#     features = df.select_dtypes(include=[np.number])
#     dist_matrix = euclidean_distances(features)
#     return dist_matrix
def calculate_min_euclidean_distances(df):
    # 分离真实数据和合成数据
    df_real = df[df['PatientID'].str.endswith('_sepsis_data')]
    df_synthetic = df[~df['PatientID'].str.endswith('_sepsis_data')]
    
    # 确保使用相同的变量
    common_columns = df_real.columns.intersection(df_synthetic.columns)
    df_real = df_real[common_columns].select_dtypes(include=[np.number])
    df_synthetic = df_synthetic[common_columns].select_dtypes(include=[np.number])
    
    min_distances = []
    for i, real_row in df_real.iterrows():
        distances = euclidean_distances([real_row], df_synthetic)
        min_distance = np.min(distances)
        if min_distance > 0:
            min_distances.append(min_distance)
    
    return min_distances