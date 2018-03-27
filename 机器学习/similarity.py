# -*- coding: utf-8 -*-
""""calc similarity"""

import math
import numpy as np
import scipy.spatial.distance as dist


def pearson(p, q):
    u"""
    皮尔逊相关性系数
    :param p: list 对象
    :param q: list 对象
    """
    # 简单求和
    sum_p = sum([float(x) for x in p])
    sum_q = sum([float(y) for y in q])

    # 求平方和
    sum_p_sq = sum([x ** 2 for x in p])
    sum_q_sq = sum([y ** 2 for y in q])

    # 求乘积之和
    sum_p_q_mul = sum([x * y for x, y in zip(p, q)])

    # 计算皮尔逊相关性系数
    num = sum_p_q_mul - (sum_p * sum_q / len(p))
    den = ((sum_p_sq - math.pow(sum_p, 2) / len(p)) * (sum_q_sq - math.pow(sum_p, 2) / len(p))) ** 0.5
    if not den:
        return 1

    return num / den


def tanimoto(p, q):
    u"""
    Tonimoto 系数，度量两个集合之间相似程度。
    :param p: list 对象
    :param q: list 对象
    """
    c = [v for v in p if v in q]
    return float(len(c)) / (len(a) + len(b) - len(c))


def cosine_similarity(p, q):
    u"""
    余弦相似度
    :param p: ndarray对象
    :param q: ndarray对象
    """
    return np.dot(p, q) / (np.linalg.norm(p) * np.linalg.norm(q))


def euclidean(p, q):
    u"""
    欧几里得距离
    :param p: ndarray对象
    :param q: ndarray对象
    """
    return math.sqrt((p - q) * ((p - q).T))


def jaccard_similarity(arr):
    u"""
    杰拉德相关性系数
    :param arr: ndarray对象
    """
    return dist.pdist(arr, "jaccard")


def manhattan_distance(p, q):
    u"""
    曼哈顿距离
    :param p: ndarray对象
    :param q: ndarray对象
    """
    return np.sum(np.abs(p - q))


def chebyshev_distance(p, q):
    u"""
    切比雪夫距离
    :param p: ndarray对象
    :param q: ndarray对象
    """
    return np.abs(p - q).max()


def hamming_distance(p, q):
    u"""
    汉明距离
    :param p: ndarray对象
    :param q: ndarray对象
    """
    smstr = np.nonzero(p - q)
    return np.shape(smstr[0])[1]
