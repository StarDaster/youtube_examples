# def func():
#     pass
#
#
# print(func)
# c = func
# print(c)

l = [1, 2, 3, 4, 5, 6]

# for el in l:
#       if case:
#           break
#     print(el)

# шаг 1 - запросить у объекта, который хотим проитерировать его итератор
# it = iter(l)  # отдать итератор
# print(type(it), type(l))
# # шаг 2 - отдать итератор в функцию next для получения очередного значения
# next_val = next(it)
# print(next_val)
# next_val = next(it)
# print(next_val)
# # del l
# # l.pop(4)
# next_val = next(it)
# print(next_val)
# next_val = next(it)
# print(next_val)
# next_val = next(it)
# print(next_val)
# next_val = next(it)
# print(next_val)
# шаг 3 - получить ошибку StopIteration для того, чтобы прекрастить итерацию

# try:
#     it = iter(l)
#     while True:
#         val = next(it)
#         print("Делаю что угодно с", val)
# except StopIteration:
#     pass

# [open("file.txt", "w") for _ in range(100_000)]

import sys


# print(sys.getsizeof([x for x in range(100_000)]))


def sample_gen_func():
    cnt = 0
    while cnt < 100_000:
        yield cnt
        cnt += 1


# g = sample_gen_func()
# print(sys.getsizeof(g))
# print(g)
# print(next(g))
# print("Получаю следующее значение")
# print(next(g))
# print("Получаю следующее значение")
# print(next(g))
# print("Получаю следующее значение")
# print(next(g))
# print("Получаю следующее значение")
# print(next(g))


class Pistol:
    def __init__(self, oboyma=None):
        self.oboyma = oboyma

    def reload(self, oboyma):
        self.oboyma = oboyma

    def shoot(self):
        if self.oboyma is not None:
            return next(self.oboyma)


def oboyma():
    print("Первый выстрел пошёл")
    yield "ПИФ-ПАФ!"
    print("Второй выстрел пошёл")
    yield "ПИФ-ПАФ!"
    print("Третий выстрел пошёл")
    yield "ПИФ-ПАФ!"
    print("Четвертый выстрел пошёл")
    yield "ПИФ-ПАФ!"
    print("Пятый выстрел пошёл")
    yield "ПИФ-ПАФ!"
    print("Патроны закончились!")


new_oboyma = oboyma()
# pistol = Pistol(new_oboyma)
# print(pistol.shoot())
# print(pistol.shoot())

# for el in new_oboyma:
#     print(el)

# it = iter(new_oboyma)
# print(it)


def my_shiny_list_iterator(l):
    cnt = 0
    while cnt < len(l):
        yield l[cnt]
        cnt += 1


it = my_shiny_list_iterator(l)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
