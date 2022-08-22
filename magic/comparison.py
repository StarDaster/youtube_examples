class SomeCuboid:
    def __init__(self, length: float, height: float):
        self.length = length
        self.height = height

    def __eq__(self, other: 'SomeCuboid') -> bool:
        print("Сравнение: равно")
        self_square = self.length * self.height
        other_square = other.length * other.height
        return self_square == other_square

    def __ne__(self, other):
        print("Сравнение: не равно")
        self_square = self.length * self.height
        other_square = other.length * other.height
        return self_square != other_square

    def __lt__(self, other):
        print("Сравнение: меньше")
        self_square = self.length * self.height
        other_square = other.length * other.height
        return self_square < other_square

    def __le__(self, other):
        print("Сравнение: меньше либо равно")
        self_square = self.length * self.height
        other_square = other.length * other.height
        return self_square <= other_square

    def __gt__(self, other):
        print("Сравнение: больше")
        self_square = self.length * self.height
        other_square = other.length * other.height
        return self_square > other_square

    def __ge__(self, other):
        print("Сравнение: больше либо равно")
        self_square = self.length * self.height
        other_square = other.length * other.height
        return self_square >= other_square


# Улучшаем код

class SomeCuboid:
    def __init__(self, length: float, height: float):
        self.length = length
        self.height = height

    @property
    def square(self):
        return self.length * self.height

    def __eq__(self, other: 'SomeCuboid') -> bool:
        if not isinstance(other, SomeCuboid):
            raise TypeError("Wrong type for comparison with SomeCuboid class: ", other.__class__)
        print("Сравнение: равно")
        return self.square == other.square

    def __ne__(self, other: 'SomeCuboid'):
        if not isinstance(other, SomeCuboid):
            raise TypeError("Wrong type for comparison with SomeCuboid class: ", other.__class__)
        print("Сравнение: не равно")
        return self.square != other.square

    def __lt__(self, other: 'SomeCuboid'):
        if not isinstance(other, SomeCuboid):
            raise TypeError("Wrong type for comparison with SomeCuboid class: ", other.__class__)
        print("Сравнение: меньше")
        return self.square < other.square

    def __le__(self, other: 'SomeCuboid'):
        if not isinstance(other, SomeCuboid):
            raise TypeError("Wrong type for comparison with SomeCuboid class: ", other.__class__)
        print("Сравнение: меньше либо равно")
        return self.square <= other.square

    def __gt__(self, other: 'SomeCuboid'):
        if not isinstance(other, SomeCuboid):
            raise TypeError("Wrong type for comparison with SomeCuboid class: ", other.__class__)
        print("Сравнение: больше")
        return self.square > other.square

    def __ge__(self, other: 'SomeCuboid'):
        if not isinstance(other, SomeCuboid):
            raise TypeError("Wrong type for comparison with SomeCuboid class: ", other.__class__)
        print("Сравнение: больше либо равно")
        return self.square >= other.square


some_cuboid_1 = SomeCuboid(10, 20)
print(some_cuboid_1.square)
some_cuboid_2 = SomeCuboid(30, 40)
print(some_cuboid_2.square)
print(some_cuboid_1 == some_cuboid_2)
print(some_cuboid_1 != some_cuboid_2)
print(some_cuboid_1 < some_cuboid_2)
print(some_cuboid_1 <= some_cuboid_2)
print(some_cuboid_1 > some_cuboid_2)
print(some_cuboid_1 >= some_cuboid_2)
