import json


def load_data(filepath):
    data = open(filepath,"r")
    data_dict = json.load(data)
    return data_dict

def pretty_print_json(data_dict):
    pretty_json = json.dumps(data_dict,indent=4,ensure_ascii=False, separators=(',', ':'))
    print(pretty_json)

if __name__ == '__main__':
    filepath = input("Ведите адрес некрасивого json-a")
    data_dict = load_data(filepath)
    pretty_print_json(data_dict)

