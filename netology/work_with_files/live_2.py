# Формат json - древовидная структура
import json


def read_json(file_name: str):
    with open(file_name) as file_object:
        data = json.load(file_object)
        return data


def write_json(in_file_name: str, out_file_name: str):
    data = read_json(in_file_name)
    with open(out_file_name, "w") as file_object:
        json.dump(data, file_object, ensure_ascii=False, indent=2)


write_json("data.json", "data_new.json")
