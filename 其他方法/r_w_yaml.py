# -*- coding: UTF-8 -*-
import os
import yaml


def read_yaml(read_path):
    u'''读取yaml文件，以字典的形式存放'''
    with open(read_path, 'r') as fr:
        return yaml.load(fr)


def write_yaml(write_path, content):
    u'''写入yaml文件'''
    with open(write_path, 'w') as fw:
        yaml.dump(content, fw)


def main(file_path, dataMap):
    write_yaml(file_path, dataMap)

    data = read_yaml(file_path)
    print data


if __name__ == "__main__":
    filename = 'test.yaml'
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

    dataMap = {'treeroot': {'branch1': {'branch1-1': {'name': 'Node 1-1'},
                                        'name': 'Node 1'},
                            'branch2': {'branch2-1': {'name': 'Node 2-1'},
                                        'name': 'Node 2'}}}

    main(file_path, dataMap)
