# говорю что хочу написать чертеж
import sys


class Matryoshka:
    MATR_GLOBAL_CNT = 0
    MATR_STORAGE = []

    def __init__(self, size, color, song, inner_matr=None):
        self.size = size
        self.color = color
        self.song = song
        self.inner_matr = inner_matr
        Matryoshka.MATR_GLOBAL_CNT += 1
        Matryoshka.MATR_STORAGE.append(self)

    def make_sound(self, repeat):
        for time in range(1, repeat + 1):
            print(f"Играет музыка {self.song} {time} раз")

    def set_inner_matr(self, matr):
        self.inner_matr = matr
        print(f"Внутренняя матрешка для {self} была задана: {matr}")

    def get_inner_matr(self):
        matr = self.inner_matr
        if matr is not None:
            return self.inner_matr
        print("Матрешки нет!")


# print(Matryoshka, sys.getsizeof(Matryoshka))
# matr_1 = Matryoshka()
# print(matr_1, sys.getsizeof(matr_1))

# matr_collection = []
# for _ in range(10):
#     matr_collection.append(Matryoshka(1, 2, 3))

# print(matr_collection)

matr_2 = Matryoshka(size=3, color="green", song="Я люблю тебя до слез")
matr_1 = Matryoshka(size=5, color="blue", song="Проклятый старый дом")
matr_1.set_inner_matr(matr_2)
matr_0 = Matryoshka(size=10, color="red", song="My Way", inner_matr=matr_1)




# print(matr_1, type(matr_1))
# print(matr_1.size, matr_1.color)
# matr_0.make_sound(3)
# matr_1.make_sound(2)

# print(Matryoshka.MATR_GLOBAL_CNT)
# print(Matryoshka.MATR_STORAGE)

print(matr_0.get_inner_matr())
