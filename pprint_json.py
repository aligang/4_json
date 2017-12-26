import json
import sys


def load_data(json_filepath):
    with open(json_filepath, "r") as file_containing_json:
        object_representing_json = json.load(file_containing_json)
    return object_representing_json


def print_pretty_json(object_representing_json):
    string_representing_pretty_json = json.dumps(
        object_representing_json,
        indent=4,
        ensure_ascii=False,
        separators=(',', ':')
    )
    print(string_representing_pretty_json)


if __name__ == '__main__':
    json_filepath = sys.argv[1]
    object_representing_json = load_data(json_filepath)
    print_pretty_json(object_representing_json)
