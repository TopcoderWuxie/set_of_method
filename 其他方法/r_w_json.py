# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import json


def read_and_write_json():
    def read_json(read_path):
        with open(read_path) as fr:
            content = json.load(fr)
        return content

    def write_json(write_path, content):
        with open(write_path, 'w') as fw:
            content = json.dumps(content, indent=2, ensure_ascii=False, sort_keys=True)
            fw.write(content)

    content = read_json('read.json')
    write_json('write.json', content)


if __name__ == "__main__":
    read_and_write_json()
