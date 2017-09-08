import json
from os import path
import sys


class NoSuchFileInDirectory(ValueError):
    pass


def load_data(filepath):
    if not path.exists(filepath) or (path.splitext(path.split(filepath)[1])[1] != '.json'):
        raise NoSuchFileInDirectory('Такого файла не существует или он не *.json')
    with open(filepath, 'r', encoding='UTF-8') as file_handler:
        return json.load(file_handler)


def pretty_print_json(data):
    pretty_print = json.dumps(load_data(data), indent=4, sort_keys=True, ensure_ascii=False)
    print(pretty_print)


if __name__ == '__main__':
    pretty_print_json(sys.argv[1])
