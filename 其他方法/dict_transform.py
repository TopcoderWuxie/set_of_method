# -*- coding: utf-8 -*-


def transform(base_data):
    ins_inv_set = set()
    for values in base_data.values():
        ins_inv_set = ins_inv_set | set(values)

    # 键值转化的键初始化
    ins_inv_dct = {key: [] for key in ins_inv_set}

    # 键值存储
    for key, values in base_data.iteritems():
        for value in values:
            ins_inv_dct[value].append(key)

    return ins_inv_dct


if __name__ == "__main__":
    data = {
        "C1": ["A1", "A2", "A4"],
        "C2": ["A2", "A3", "A4"],
        "C3": ["A1", "A3", "A4"]
    }

    data = transform(data)

    print data
