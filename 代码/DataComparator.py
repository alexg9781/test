from correlation.correlation import CorrelationAnalyzer
from ftest.ftest import FTestAnalyzer
from ks_test.ks_test import KSTestAnalyzer
from ttest.ttest import TTestAnalyzer
from attribute_inference_risk.attribute_inference_risk import attribute_inference_risk
from calculate_euclidean_distances import calculate_euclidean_distances
from membership_inference_risk.membership_inference_risk import membership_inference_risk
from reidentification_risk.reidentification_risk import reidentification_risk
import matplotlib.pyplot as plt
import seaborn as sns

class DataComparator:
    def __init__(self, df_real, df_synthetic):
        self.df_real = df_real
        self.df_synthetic = df_synthetic

    def correlation(self, method='pearson'):
        if method not in ['pearson', 'spearman']:
            raise ValueError("Method must be either 'pearson' or 'spearman'")
        
        analyzer = CorrelationAnalyzer(self.df_real, self.df_synthetic)
        if method == 'pearson':
            pearson_results, _ = analyzer.analyze_tests()
            return pearson_results
        else:
            _, spearman_results = analyzer.analyze_tests()
            return spearman_results

    def plot_correlation_heatmap(self, correlation_matrix, title='Correlation Heatmap'):
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
        plt.title(title)
        plt.show()

    def ks_test(self):
        analyzer = KSTestAnalyzer(self.df_real, self.df_synthetic)
        ks_test_results = analyzer.analyze_tests()
        return ks_test_results

    def ttest(self, group_col):
        analyzer = TTestAnalyzer(self.df_real, self.df_synthetic)
        real_t_test_results, synthetic_t_test_results = analyzer.analyze_tests(group_col)
        combined_results = self._combine_test_results(real_t_test_results, synthetic_t_test_results)
        return combined_results

    def ftest(self, group_col):
        analyzer = FTestAnalyzer(self.df_real, self.df_synthetic)
        real_f_test_results, synthetic_f_test_results = analyzer.analyze_tests(group_col)
        combined_results = self._combine_test_results(real_f_test_results, synthetic_f_test_results)
        return combined_results

    def _combine_test_results(self, real_results, synthetic_results):
        combined_results = {
            'real': real_results,
            'synthetic': synthetic_results
        }
        return combined_results

    # 属性推断风险
    def attribute_inference_risk(self, df, attribute):
        attribute_risk = attribute_inference_risk(df, attribute)
        return attribute_risk

    # 计算欧几里得距离
    def calculate_euclidean_distances(self, df):
        euclidean_dist_matrix = calculate_euclidean_distances(df)
        return euclidean_dist_matrix

    # 成员推断风险
    def membership_inference_risk(self, df):
        membership_risk = membership_inference_risk(df)
        return membership_risk

    # 再识别风险
    def reidentification_risk(self, df, unique_identifier):
        reidentification_risk_value = reidentification_risk(df, unique_identifier)
        return reidentification_risk_value
