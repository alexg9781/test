import numpy as np
from sklearn.metrics.pairwise import euclidean_distances

# 计算欧几里得距离
def calculate_euclidean_distances(df):
    features = df.select_dtypes(include=[np.number])
    dist_matrix = euclidean_distances(features)
    return dist_matrix