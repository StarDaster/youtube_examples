# Формат CSV - плоские данные
# import csv
#
#
# def read_csv(file_name: str):
#     with open(file_name) as csv_file:
#         reader = csv.reader(csv_file)
#         print(reader)
#         data = list(reader)
#         print(data)
#     header = data.pop(0)
#     print(header)
#     return header, data
#
#
# def read_csv_as_dict(file_name: str):
#     with open(file_name) as csv_file:
#         reader = csv.DictReader(csv_file)
#         print(reader)
#         for item in reader:
#             print(item)
#
#
# def write_csv(in_file_name: str, out_file_name: str):
#     header, data = read_csv(in_file_name)
#
#     with open(out_file_name, "w") as file:
#         writer = csv.writer(file, delimiter=";")
#         writer.writerow(header)
#         writer.writerows(data)
#
#
# # read_csv("sample.csv")
# # write_csv("sample.csv", "sample_new.csv")
# read_csv_as_dict("sample.csv")


# # Формат XML - древовидная структура
# import xml.etree.ElementTree as ET
# from xml.dom import minidom
#
# parser = ET.XMLParser(encoding="utf-8")
# tree = ET.parse("sample.xml", parser)
# root = tree.getroot()
# print(root.text, root.tag, root.attrib["version"])
#
# books_list = root.findall("book")
# author_list = root.findall("book/author")
# print(books_list)
# print(author_list)
# for book in books_list:
#     print(book.find("author"))
#     print(book.attrib["id"])
#
# xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="    ")
# with open("result.xml", "w") as file_object:
#     file_object.write(xmlstr)

# Формат json - древовидная структура
# import json
#
#
# def read_json(file_name: str):
#     with open(file_name) as file_object:
#         data = json.load(file_object)
#         print(data)
#         return data
#
#
# def write_json(in_file_name: str, out_file_name: str):
#     data = read_json(in_file_name)
#     with open(out_file_name, "w") as file:
#         json.dump(data, file, ensure_ascii=False, indent=2)
#
#
# # read_json("data.json")
# write_json("data.json", "data_new.json")
