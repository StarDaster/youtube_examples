"""
Вам нужно помочь секретарю автоматизировать работу. Для этого нужно написать программу, которая будет на основе
хранимых данных исполнять пользовательские команды.

Исходные данные имеют следующую структуру:

1.Перечень всех документов

documents = [
 {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
 {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
 {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]
2.Перечень полок, на которых хранятся документы (если документ есть в documents, то он обязательно должен быть и
в directories)

directories = {
 '1': ['2207 876234', '11-2'],
 '2': ['10006'],
 '3': []
}
"""

documents = [
 {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
 {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
 {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
 '1': ['2207 876234', '11-2'],
 '2': ['10006'],
 '3': []
}


def get_user_by_document_number(document_number: str):
    """Задание 1"""
    for document in documents:
        if document["number"] == document_number:
            return document["name"]


def get_shelf_by_document_number(document_number: str):
    """Задание 2"""
    for shelf in directories.items():
        if document_number in shelf[1]:
            return shelf[0]


def get_full_info():
    """Задание 3"""
    for document in documents:
        shelf = get_shelf_by_document_number(document["number"])
        print(f"№: {document['number']}, "
              f"тип: {document['type']}, "
              f"владелец: {document['name']}, "
              f"полка хранения: {shelf}")

def get_shelfs_info():
    return ", ".join(directories.keys())

def add_new_shelf(shelf_number: str):
    """Задание 4"""
    if shelf_number in directories:
        print(f"Такая полка уже существует! Текущий перечень полок: {get_shelfs_info()}.")
        return
    directories[shelf_number] = []
    print(f"Полка добавлена. Текущий перечень полок: {get_shelfs_info}.")


def delete_shelf(shelf_number: str):
    data_from_shelf = directories.get(shelf_number)
    if data_from_shelf == []:
        del directories[shelf_number]
        print(f"Полка удалена. Текущий перечень полок: {get_shelfs_info()}.")
    else:
        print(f"На полке есть документа, удалите их перед удалением полки. "
              f"Текущий перечень полок: {get_shelfs_info()}.")


command = input("Введите команду: ")
if command == "p":
    document_number = input("Введите номер документа: ")
    user = get_user_by_document_number(document_number)
    if user is None:
        print("Документ не найден в базе")
    else:
        print("Владелец документа:", user)
elif command == "s":
    document_number = input("Введите номер документа: ")
    shelf = get_shelf_by_document_number(document_number)
    if shelf is None:
        print("Документ не найден в базе")
    else:
        print("Документ хранится на полке:", shelf)
elif command == "l":
    get_full_info()
elif command == "ads":
    shelf_number = input("Введите номер полки: ")
    add_new_shelf(shelf_number)
