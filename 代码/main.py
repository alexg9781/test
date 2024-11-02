import pandas as pd
import numpy as np
from scipy.stats import ttest_ind
from scipy.stats import f_oneway
from scipy.stats import ks_2samp
from scipy.stats import pearsonr

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from tabulate import tabulate


# 比较基本统计数据
def average_analyse():
    for real_col, synthetic_col in columns_to_compare.items():
        print(f"Comparing {real_col} and {synthetic_col}")
        print(
            f"Real Data - Mean: {real_data[real_col].mean()}, Median: {real_data[real_col].median()}"
        )
        print(
            f"Synthetic Data - Mean: {synthetic_data[synthetic_col].mean()}, Median: {synthetic_data[synthetic_col].median()}"
        )
        print("\n")


def t_test(real_file, synthetic_file):
    real_data = pd.read_csv(real_file)
    synthetic_data = pd.read_csv(synthetic_file)
    real_data_headers_list = real_data.columns.tolist()
    synthetic_data_headers_list = synthetic_data.columns.tolist()

    results = []
    for real_col in real_data_headers_list:
        for synthetic_col in synthetic_data_headers_list:
            real_data_column = real_data[real_col].dropna()
            synthetic_data_column = synthetic_data[synthetic_col].dropna()

            t_statistic, p_value = ttest_ind(real_data_column, synthetic_data_column)
            # 将结果添加到列表中
            results.append(
                [len(results) + 1, real_col, synthetic_col, t_statistic, p_value]
            )
            break
            # print(
            #     f"[Function t_test] Comparing {real_col} and {synthetic_col}",
            #     f"t-statistic: {t_statistic}, p-value: {p_value}",
            # )
            # if p_value < 0.05:
            #     print(
            #         f"The means of {real_col} and {synthetic_col} are significantly different at the 0.05 significance level."
            #     )
            # else:
            #     print(
            #         f"The means of {real_col} and {synthetic_col} are not significantly different at the 0.05 significance level.\n"
            #     )
    print(
        tabulate(
            results,
            headers=["Real Column", "Synthetic Column", "t-statistic", "p-value"],
            tablefmt="fancy_grid",
        )
    )


def f_test(real_file, synthetic_file):
    real_data = pd.read_csv(real_file)
    synthetic_data = pd.read_csv(synthetic_file)

    real_data_headers_list = real_data.columns.tolist()
    synthetic_data_headers_list = synthetic_data.columns.tolist()

    for real_col in real_data_headers_list:
        for synthetic_col in synthetic_data_headers_list:
            real_data_column = real_data[real_col].dropna()
            synthetic_data_column = synthetic_data[synthetic_col].dropna()
            f_statistic, p_value = f_oneway(real_data_column, synthetic_data_column)

            print(
                f"[Function f_test] Comparing {real_col} and {synthetic_col}",
                f"F-statistic: {f_statistic}, p-value: {p_value}",
            )


def ks_test(real_file, synthetic_file):
    real_data = pd.read_csv(real_file)
    synthetic_data = pd.read_csv(synthetic_file)

    real_data_headers_list = real_data.columns.tolist()
    synthetic_data_headers_list = synthetic_data.columns.tolist()

    for real_col in real_data_headers_list:
        for synthetic_col in synthetic_data_headers_list:
            real_data_column = real_data[real_col].dropna()
            synthetic_data_column = synthetic_data[synthetic_col].dropna()

            # 执行 KS 检验
            ks_statistic, p_value = ks_2samp(real_data_column, synthetic_data_column)

            print(
                f"[Function ks_test] Comparing {real_col} and {synthetic_col}",
                f"KS statistic: {ks_statistic}, p-value: {p_value}",
            )


def correlation_test(real_file, synthetic_file):
    real_data = pd.read_csv(real_file)
    synthetic_data = pd.read_csv(synthetic_file)
    real_data_headers_list = real_data.columns.tolist()
    synthetic_data_headers_list = synthetic_data.columns.tolist()

    for real_col in real_data_headers_list:
        for synthetic_col in synthetic_data_headers_list:
            real_data_column = real_data[real_col].dropna()
            synthetic_data_column = synthetic_data[synthetic_col].dropna()

            min_length = min(len(real_data_column), len(synthetic_data_column))
            if min_length == 0:
                print(
                    f"[Function correlation_test] No valid data for {real_col} and {synthetic_col}."
                )
                continue

            # 取最小长度的数据进行相关性计算
            real_data_column = real_data_column.iloc[:min_length]
            synthetic_data_column = synthetic_data_column.iloc[:min_length]

            # 执行皮尔逊相关性检验
            corr_coefficient, p_value = pearsonr(
                real_data_column, synthetic_data_column
            )

            # 打印结果
            print(
                f"[Function correlation_test] Comparing {real_col} and {synthetic_col}",
                f"Correlation coefficient: {corr_coefficient}, p-value: {p_value}",
            )


def membership_inference_attack_test(real_file, synthetic_file, threshold=0.5):
    real_data = pd.read_csv(real_file)
    synthetic_data = pd.read_csv(synthetic_file)

    real_data_headers_list = real_data.columns.tolist()
    synthetic_data_headers_list = synthetic_data.columns.tolist()

    for real_col in real_data_headers_list:
        for synthetic_col in synthetic_data_headers_list:
            real_data_column = real_data[real_col].dropna()
            synthetic_data_column = synthetic_data[synthetic_col].dropna()

            real_confidence = np.random.rand(len(real_data_column))
            synthetic_confidence = np.random.rand(len(synthetic_data_column))

            # 进行会员推断
            real_membership_inference = real_confidence > threshold
            synthetic_membership_inference = synthetic_confidence > threshold

            print(
                f"[Function membership_inference_attack_test] Comparing {real_col} and {synthetic_col}",
                f"Real data membership inference: {real_membership_inference.sum()} members detected",
                f"Synthetic data membership inference: {synthetic_membership_inference.sum()} members detected",
            )


def reidentification_risk_test(data_file):
    data = pd.read_csv(data_file)

    headers_list = data.columns.tolist()

    # 计算 k-anonymity
    k_anonymity = {}
    for col in headers_list:
        # 计算每个列的 k-anonymity
        k_value = data[col].value_counts().min()
        k_anonymity[col] = k_value

    # 输出 k-anonymity 结果
    print("[Function reidentification_risk_test] K-anonymity values:")
    results = []
    for col, k_value in k_anonymity.items():
        # print(f"{col}: {k_value}")
        results.append([len(results) + 1, col, k_value])
    print(
        tabulate(
            results,
            headers=["Real col", "k_value"],
            tablefmt="fancy_grid",
        )
    )

    # 计算 l-diversity
    l_diversity = {}
    for col in headers_list:
        # 对于每个敏感属性，计算其 l-diversity
        sensitive_values = data[col].dropna().unique()
        l_value = len(sensitive_values)
        l_diversity[col] = l_value

    # 输出 l-diversity 结果
    print("[Function reidentification_risk_test] L-diversity values:")
    results = []

    for col, l_value in l_diversity.items():
        # print(f"{col}: {l_value}")
        results.append([len(results) + 1, col, l_value])
    print(
        tabulate(
            results,
            headers=["Real col", "l_value"],
            tablefmt="fancy_grid",
        )
    )


def calculate_euclidean_distances(data_file):
    data = pd.read_csv(data_file)
    num_samples = data.shape[0]
    distances = np.zeros((num_samples, num_samples))  # 初始化距离矩阵

    # 计算每对样本之间的欧氏距离
    for i in range(num_samples):
        for j in range(num_samples):
            if i != j:
                distances[i][j] = np.sqrt(np.sum((data.iloc[i] - data.iloc[j]) ** 2))
            else:
                distances[i][j] = 0.0  # 自身到自身的距离为0
        print(
            f"[Function calculate_euclidean_distances] data is {data_file} Euclidean distances: {distances}"
        )
    return distances


def attribute_inference_risk_test(
    real_file, synthetic_file, sensitive_col="Admn001_ID"
):
    real_data = pd.read_csv(real_file)
    synthetic_data = pd.read_csv(synthetic_file)

    # 获取数据列名
    # real_data_headers_list = real_data.columns.tolist()
    # synthetic_data_headers_list = synthetic_data.columns.tolist()

    # 遍历真实数据和合成数据的每一列
    # for real_col in real_data_headers_list:
    #     for synthetic_col in synthetic_data_headers_list:
    #         real_data_column = real_data[real_col].dropna()
    #         synthetic_data_column = synthetic_data[synthetic_col].dropna()

    #         # 计算属性推断成功率（这里简单模拟为随机数，实际应用中应使用模型输出） mock todo
    #         inference_success_rate = np.random.rand()  # 模拟推断成功率
    #         # 打印结果
    #         print(
    #             f"[Function attribute_inference_risk_test] {i} Comparing {real_col} and {synthetic_col}",
    #             f"Inference success rate: {inference_success_rate:.2f}",
    #         )
    ##########################################################################

    # 获取特征列（去掉目标列）
    feature_cols = [col for col in real_data.columns if col != sensitive_col]

    # # 分离特征和目标变量
    X = real_data[feature_cols]
    y = real_data[sensitive_col]

    # # 拆分数据集为训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # # 创建并训练逻辑回归模型
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # # 用测试集进行预测
    y_pred = model.predict(X_test)

    # 计算准确率和混淆矩阵
    accuracy = accuracy_score(y_test, y_pred)
    # cm = confusion_matrix(y_test, y_pred)
    print(f"Model Accuracy: {accuracy:.2f}")
    # print("Confusion Matrix:", cm)

    # # 对合成数据进行预测
    synthetic_data_column = synthetic_data[feature_cols]

    # # 预测合成数据的目标属性
    synthetic_predictions = model.predict(synthetic_data_column)

    # # 计算属性推断成功率（这里以预测正确的比例作为成功率）
    inference_success_rate = np.mean(
        synthetic_predictions == synthetic_data[sensitive_col]
    )

    print(f"Inference Success Rate: {inference_success_rate:.2f}")


if __name__ == "__main__":
    real_file = "../数据/ZZZ_Sepsis_Data_From_R.csv"
    synthetic_file = "../数据/C001_FakeSepsis.csv"  # C001_FakeHypotension.csv

    # t_test(real_file, synthetic_file)
    # f_test(real_file, synthetic_file)
    # ks_test(real_file, synthetic_file)
    # calculate_euclidean_distances(real_file)  # calc 无需处理 todoing
    # correlation_test(real_file, synthetic_file)
    # membership_inference_attack_test(real_file, synthetic_file)
    # reidentification_risk_test(synthetic_file)

    # todo
    attribute_inference_risk_test(real_file, synthetic_file)
