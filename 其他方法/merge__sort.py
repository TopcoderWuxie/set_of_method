# -*- coding: utf-8 -*-

"""
归并排序：数据先分后合
"""


def merge(lstA, lstB):
    i, j = 0, 0
    lst = []
    while i < len(lstA) and j < len(lstB):
        if lstA[i] < lstB[j]:
            lst.append(lstA[i])
            i += 1
        else:
            lst.append(lstB[j])
            j += 1

    while i < len(lstA):
        lst.append(lstA[i])
        i += 1

    while j < len(lstB):
        lst.append(lstB[j])
        j += 1

    return lst


def merge_sort(data):
    mid = len(data) / 2
    if mid == 0:  # 只剩少于或等于一条数据的时候不能再拆分，直接返回
        return data
    lstA = merge_sort(data[:mid])
    lstB = merge_sort(data[mid:])

    return merge(lstA, lstB)


if __name__ == "__main__":
    data = [3, 4, 2, 7, 6, 9, 5, 8, 1]
    print merge_sort(data)  # 输出结果：[1, 2, 3, 4, 5, 6, 7, 8, 9]

