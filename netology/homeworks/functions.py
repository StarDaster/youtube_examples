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
    """Получить пользователя по номеру документа"""
    for document in documents:
        if document["number"] == document_number:
            return document["name"]


def get_shelf_by_document_number(document_number: str):
    """Пункт 2 - получить полку по номеру документа"""
    for shelf in directories.items():
        if document_number in shelf[1]:
            return shelf[0]


def get_full_info():
    """Пункт 3 - получение полной информации"""
    for document in documents:
        shelf = get_shelf_by_document_number(document["number"])
        print(f"№: {document['number']}, "
              f"тип: {document['type']}, "
              f"владелец: {document['name']}, "
              f"полка хранения: {shelf}")


def get_shelfs_info():
    return ", ".join(directories.keys())


def add_new_shelf(shelf_number: str):
    """Пункт 4 - добавление полки"""
    if shelf_number in directories:
        print(f"Такая полка уже существует! Текущий перечень полок: {get_shelfs_info()}.")
        return
    directories[shelf_number] = []
    print(f"Полка добавлена. Текущий перечень полок: {get_shelfs_info}.")


def delete_shelf(shelf_number: str):
    """Пункт 5 - удаление полки"""
    data_from_shelf = directories.get(shelf_number)
    if data_from_shelf == []:
        del directories[shelf_number]
        print(f"Полка удалена. Текущий перечень полок: {get_shelfs_info()}.")
    elif data_from_shelf is None:
        print(f"Такой полки не существует. Текущий перечень полок: {get_shelfs_info()}.")
    else:
        print(f"На полке есть документа, удалите их перед удалением полки. "
              f"Текущий перечень полок: {get_shelfs_info()}.")


"""Дополнительная часть"""


def add_new_document_to_shelf():
    """Пользователь по команде “ad” может добавить новый документ в данные"""
    document_number = input("Введите номер документа: ")
    document_type = input("Введите тип документа: ")
    user = input("Введите владельца документа: ")
    shelf_number = input("Введите полку для хранения: ")
    if shelf_number not in directories:
        print(f"Такой полки не существует. Добавьте полку командой as.")
        return
    document_data = {
        'type': document_type,
        'number': document_number,
        'name': user
    }
    documents.append(document_data)
    directories[shelf_number].append(document_number)
    print("Документ добавлен. Текущий список документов:")
    get_full_info()


def delete_document(document_number: str):
    shelf_number = get_shelf_by_document_number(document_number)
    if shelf_number is None:
        print("Документ не найден в базе.")
        get_full_info()
        return
    directories[shelf_number].remove(document_number)
    for document in documents:
        if document["number"] == document_number:
            documents.remove(document)
    print("Документ удален.")
    get_full_info()


def move_document():
    current_document_number = input("Введите номер документа: ")
    shelf_number = input("Введите номер полки: ")
    current_shelf_number = get_shelf_by_document_number(current_document_number)
    if shelf_number is None:
        print("Документ не найден в базе.")
        get_full_info()
        return
    if directories.get(shelf_number) is None:
        print(f"Такой полки не существует. Текущий перечень полок: {get_shelfs_info()}.")
        return
    for document_number in directories[current_shelf_number]:
        if document_number == current_document_number:
            directories[current_shelf_number].remove(document_number)
            directories[shelf_number].append(document_number)
    print("Документ перемещен. ")
    get_full_info()


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
elif command == "ad":
    add_new_document_to_shelf()
elif command == "d":
    document_number = input("Введите номер документа: ")
    delete_document(document_number)
elif command == "m":
    move_document()
