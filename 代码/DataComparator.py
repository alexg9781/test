from correlation import CorrelationAnalyzer
from ftest import FTestAnalyzer
from ks_test import KSTestAnalyzer
from ttest import TTestAnalyzer
from attribute_inference_risk import attribute_inference_risk
from calculate_euclidean_distances import calculate_euclidean_distances
from membership_inference_risk import membership_inference_risk
from reidentification_risk import reidentification_risk


class DataComparator:
    def __init__(self, df_real, df_synthetic):
        self.df_real = df_real
        self.df_synthetic = df_synthetic

    def correlation(self):
        analyzer = CorrelationAnalyzer(self.df_real, self.df_synthetic)
        pearson_results, spearman_results = analyzer.analyze_tests()
        return pearson_results, spearman_results

    def ftest(self, group_col):
        analyzer = FTestAnalyzer(self.df_real, self.df_synthetic)
        real_f_test_results, synthetic_f_test_results = analyzer.analyze_tests(group_col)
        return real_f_test_results, synthetic_f_test_results

    def ks_test(self):
        analyzer = KSTestAnalyzer(self.df_real, self.df_synthetic)
        ks_test_results = analyzer.analyze_tests()
        return ks_test_results

    def ttest(self, group_col):
        analyzer = TTestAnalyzer(self.df_real, self.df_synthetic)
        real_t_test_results, synthetic_t_test_results = analyzer.analyze_tests(group_col)
        return real_t_test_results, synthetic_t_test_results

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
