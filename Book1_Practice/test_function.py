# coding:utf-8
import math
"""
用户u 物品i
rui: 用户u对物品i的实际评分
pui: 用户u对物品i的预测评分
1. 评分预测 RMSE and MAE
2. TopN推荐 准确率(precision）and 召回率(recall) 
"""


class Test_Function:
    # 均方根误差
    def RMSE(self, records):
        """
        :param records:list{records[i] = [u, i, rui, pui]}
        :return: rmse
        """
        return math.sqrt(sum([(rui - pui) * (rui - pui) for u, i, rui, pui in records]) / float(len(records)))

    # 平均绝对误差
    def MAE(self, records):
        """
        :param records: :list{records[i] = [u, i, rui, pui]}
        :return: mae
        """
        return sum([abs(rui - pui) for u, i, rui, pui in records]) / float(len(records))

    # TopN
    def PrecisionRecall(self, test, N):
        hit = 0
        n_recall = 0
        n_precision = 0
        for user, items in test.items():
            rank = self.Recommand(user, N)       # !!!未定义
            hit += len(rank & items)
            n_recall += len(items)
            n_precision += N
        return [hit / (1.0 * n_recall), hit / (1.0 * n_precision)]

