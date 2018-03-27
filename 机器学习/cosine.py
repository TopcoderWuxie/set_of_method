# -*- coding: utf-8 -*-
u"""
利用稀疏矩阵求余弦相似度

问题来源：
    1. 数据量大
    2. 数据稀疏

利用稀疏矩阵的目的：
    1. 避免内存开销过大
    2. 减少开发时间

存在问题：
    最终生成的稀疏矩阵数据量同样很大，可能存在计算出结果后撑爆内存的风险。（待测试）
"""
from operator import itemgetter
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity


class Similarity(object):
    def __init__(self, number=100):
        # 保留前num条数据
        self.number = number

        # 投资机构编号
        self.investor_dct = {}
        # 被投资公司编号
        self.company_dct = {}

        self.base_data = self.load_data()

    def __call__(self):
        self.base_data = self.transform()

        csr_mat = self.set_csr_matrix()

        csr_mat = self.calc_cosine(csr_mat)

        self.trans_out(csr_mat)

    @staticmethod
    def load_data():
        u"""数据获取"""
        data = {
            "C1": ["A2", "A2", "A2", "A4"],
            "C2": ["A2", "A3", "A4"],
            "C3": ["A1", "A3", "A4"]
        }

        return data

    @staticmethod
    def save_data(key, value):
        u"""
        改为把数据保存即可

        真实场景中保存到mongo中
        :param key: 当前处理的数据行名称
        :param value: 与其相似的前number条数据，每条数据都是使用(数据行名称， 余弦相似度)
        """
        print key, value

    def transform(self):
        u"""
        直接得到的数据不能直接使用，要通过一定策略进行转化。

        字典键值转化

        {key1: [value1, value2], key2: [value1]} --> {value1: [key1, key2], value2: [key1]}
        :return: 转化后的数据
        """
        ins_inv_set = set()
        for values in self.base_data.values():
            ins_inv_set = ins_inv_set | set(values)

        self.company_dct = self.get_dct(self.base_data.keys())
        self.investor_dct = self.get_dct(list(ins_inv_set))

        # 初始化
        ins_inv_dct = {key: [] for key in ins_inv_set}
        # 键值存储
        for key, values in self.base_data.iteritems():
            for value in values:
                ins_inv_dct[value].append(key)

        return ins_inv_dct

    def set_csr_matrix(self):

        def get_row_col(base_data, investor_dct, company_dct):
            u"""
            :param base_data: 数据集
            :param investor_dct: 投资机构编号
            :param company_dct: 被投资公司编号
            :return: 对应位置元素值,(行索引下标list,列索引下标list)
            """
            row = []
            col = []
            prob = []

            for key, values in base_data.iteritems():
                for value in set(values):
                    row.append(investor_dct.get(key))
                    col.append(company_dct.get(value))
                    prob.append(values.count(value))

            # 在这里对数据归一化
            # TODO 归一化方式：d / (max - min)
            _max = max(prob)
            _min = min(prob)
            if _max != _min:
                prob = [d * 1.0 / (_max - _min) for d in prob]

            return prob, (row, col)

        data = get_row_col(self.base_data, self.investor_dct, self.company_dct)

        csr_arr = csr_matrix(data)
        return csr_arr

    @staticmethod
    def calc_cosine(csr_arr):
        # dense_output 设置输出类型，稠密还是稀疏，这里设置为输出稀疏矩阵
        return cosine_similarity(csr_arr, dense_output=False)

    def trans_out(self, csr_mat):
        u"""
        输出结果处理，详情见输出
        :param csr_mat: 余弦相似度对应的稀疏矩阵结果集
        """

        ins_k_v_trans = self.k_v_transform(self.investor_dct)
        for x, mat in enumerate(csr_mat):
            indices = mat.indices
            output_data = []
            key = ins_k_v_trans.get(x)
            for index in indices:
                output_data.append(tuple([ins_k_v_trans.get(index), mat[0, index]]))

            output_data = sorted(output_data, key=itemgetter(1), reverse=True)[1:]
            self.save_data(key, output_data[:self.number])

    @staticmethod
    def get_dct(data):
        u"""对字典的键设置编号"""
        return {key: value for key, value in zip(data, range(len(data)))}

    @staticmethod
    def k_v_transform(_dict):
        u"""键值反转"""
        return {value: key for key, value in _dict.iteritems()}


if __name__ == "__main__":
    sim = Similarity(10)
    sim()
