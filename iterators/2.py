# tumb = ["ножницы", "карандаш", "яблоко", "книга"]
# iter(tumb)
# for el in tumb:
#     print(el)
from typing import List


class MyCustomIterator:
    def __init__(self, stuff):
        self.stuff = stuff
        self.current = -1

    def to_start(self):
        self.current = -1

    def to_custom(self, custom):
        self.current = custom

    def __iter__(self):
        return self

    def __next__(self):
        while self.current < len(self.stuff) - 1:
            self.current += 1
            return self.stuff[self.current]
        raise StopIteration


class Tumbochka(List):
    """Волшебная тумбочка с тремя ящиками для чего угодно"""

    def add_to_box(self, obj):
        self.append(obj)
        # if box_num not in self.boxes:
        #     print("Вы ввели неправильный номер ящика!")
        # else:
        #     self.boxes[box_num].append(obj)

    def remove_from_box(self):
        self.pop()
        # if box_num not in self.boxes:
        #     print("Вы ввели неправильный номер ящика!")
        # else:
        #     return self.boxes[box_num].pop()

    # def __str__(self):
        # boxes_items = self.boxes[1] + self.boxes[2] + self.boxes[3]
        # return ", ".join(boxes_items)


    # def __iter__(self):
    #     it = MyCustomIterator(self.boxes[1] + self.boxes[2] + self.boxes[3])
    #     return it


tumb = Tumbochka()
tumb.add_to_box("ножницы")
tumb.add_to_box("карандаш")
tumb.add_to_box("яблоко")
tumb.add_to_box("книга")

it = iter(tumb)
print(it)

tumb.append(123)

try:
    while True:
        value = next(it)
        print(value)
        # answ = input("to custom? ")
        # if answ != "":
        #     it.to_custom(int(answ))
except StopIteration:
    pass


# for el in tumb:
#     print(el)

# print(iter(tumb))

# my_shiny_list = [
#     ["Это", "список", "внутри", "списка"],
#     {"Это", "множество", "внутри", "списка"},
#     "Это строка внутри списка",
#     tumb,
# ]
#
# for some_collection in my_shiny_list:
#     if isinstance(some_collection, Tumbochka):
#         for el in some_collection.boxes.items():
#             print(el)
#     else:
#         for el in some_collection:
#             print(el)


# def sample():
#     yield
#
#
# print(sample())
# print(iter(sample()))
