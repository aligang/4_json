import json

def load_data(json_filepath):
    file_containing_json = open(json_filepath,"r")
    dict_representing_json = json.load(file_containing_json)
    return dict_representing_json

def print_pretty_json(dict_representing_json):
    string_representing_pretty_json = json.dumps(dict_representing_json,
                                                 indent=4,
                                                 ensure_ascii=False,
                                                 separators=(',', ':'))
    print(string_representing_pretty_json)

if __name__ == '__main__':
    json_filepath = input("Укажите файл, где хранится некрасивый  json :")
    dict_representing_json = load_data(json_filepath)
    print_pretty_json(dict_representing_json)

