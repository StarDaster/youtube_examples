# file_object = open(file="sample_file.txt", mode="r")
# print(file_object.tell())
# all_from_file = file_object.read()
# print(all_from_file)
# print(file_object.seek(0))
# all_lines_from_file = file_object.readlines()
# print(file_object.tell())
# print(all_lines_from_file)
# line = file_object.readline()
# print(line)
# line = file_object.readline()
# print(line)
# file_object.close()

# [open(file="sample_file.txt", mode="r") for _ in range(100_000)]

# class A:
#     def __enter__(self):
#         print("Начали что-то делать")
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("Закончили что-то делать")
#
#
# a = A()


# with a:
#     print("Контекст")


# with open(file="sample_file.txt", mode="r") as file_object:
#     print(file_object)
#     for line in file_object:
#         print(line)
# print("Программа завершена!")

users = [
    "Peter Petrov Manager\n",
    "Sviridov Nikolai Developer\n",
    "Ivan Ivanov Developer\n"
]
user = "Peter Petrov Manager"

try:
    with open(file="sample_file_3.txt", mode="r", encoding="UTF-8") as file_object:
        file_object.write(f"\n{user}")
        file_object.writelines(users)
except FileNotFoundError as err:
    print("Файл не найден!", err)
