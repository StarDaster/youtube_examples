# tumb = ["ножницы", "карандаш", "яблоко", "книга"]

# for obj in tumb:
#     print(obj)

# print(iter(tumb))

# tumb = ["ножницы", "карандаш", "яблоко", "книга"]

# получаем итератор для итерируемого объекта
# it = iter(tumb)

# try:
#     while True:
#         next_val = next(it)
#         print("Очередное значение:", next_val)
# except StopIteration:
#     # явно напечатаем сообщение об окончании итерации,
#     # хотя цикл for этого не делает и ошибка просто подавляется
#     print("Итерация закончена")
# print("Программа завершена")


class Tumbochka:
    """Волшебная тумбочка с тремя ящиками для чего угодно"""

    def __init__(self):
        self.boxes = {
            1: [],
            2: [],
            3: []
        }

    def add_to_box(self, obj, box_num):
        if box_num not in {1, 2, 3}:
            print("Вы ввели неправильный номер ящика!")
        else:
            self.boxes[box_num].append(obj)

    def remove_from_box(self, box_num):
        if box_num not in {1, 2, 3}:
            print("Вы ввели неправильный номер ящика!")
        else:
            return self.boxes[box_num].pop()

    def __str__(self):
        boxes_items = self.boxes[1] + self.boxes[2] + self.boxes[3]
        return ", ".join(boxes_items)

    def __iter__(self):
        # получаем сумму предметов всех ящиков
        boxes_items = self.boxes[1] + self.boxes[2] + self.boxes[3]
        # получаем итератор от списка и возвращаем его
        it = iter(boxes_items)
        return it


tumb = Tumbochka()
tumb.add_to_box("ножницы", 1)
tumb.add_to_box("карандаш", 2)
tumb.add_to_box("яблоко", 3)
tumb.add_to_box("книга", 1)
print(tumb)

my_shiny_list = [
    ["Это", "список", "внутри", "списка"],
    {"Это", "множество", "внутри", "списка"},
    "Это строка внутри списка",
    tumb,
]

for some_collection in my_shiny_list:
    for el in some_collection:
        print(el)

