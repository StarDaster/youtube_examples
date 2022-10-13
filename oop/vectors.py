# vect_1 = [0, 1]
# vect_2 = [1, 5]
#
#
# def mod_vect(vector: list) -> float:
#     return ((vector[0] ** 2) + (vector[1] ** 2)) ** 0.5
#
#
# def get_vector_info(vector: list) -> str:
#     return f"Координата x: {vector[0]}\nКоордината y: {vector[1]}"
#
#
# print(get_vector_info(vector=vect_1))
# print(mod_vect(vector=vect_1))


class Vector2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def mod_vect(self) -> float:
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return f"Координата x: {self.x}\nКоордината y: {self.y}"

    def __add__(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(x=self.x + other.x, y=self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y


vect_1 = Vector2D(1, 2)
vect_2 = Vector2D(3, 4)
vect_3 = vect_1 + vect_2 + vect_2 + vect_2 + vect_2
print(vect_3)
print(vect_1 <= vect_1)


class Mixin:
    def __str__(self):
        return f"Это объект типа {type(self)}"

    def get_memory_address(self):
        return f"Адрес в памяти: {id(self)}"


class Vector3D(Mixin, Vector2D):
    def __init__(self, x: float, y: float, z: float):
        super().__init__(x, y)
        self.z = z

    def mod_vect(self) -> float:
        return ((self.x ** 2) + (self.y ** 2) + (self.z ** 2)) ** 0.5

    # def __str__(self):
    #     return f"{super().__str__()}\nКоордината z: {self.z}"


# class Vector3D_2(Vector2D):
#     def __str__(self):
#         return f"Координата x: {self.x}\nКоордината y: {self.y}\nКоордината z: {self.z}"


# vect_data = [1, 5]
# vect_data_dict = {"x": 1, "y": 5}
# vector = Vector(vect_data[0], vect_data[1])
# vector_1 = Vector(*vect_data)
# vector_2 = Vector(**vect_data_dict)

# vector2d = Vector2D(x=1, y=5)
# print(vector2d.mod_vect())
# print(vector2d)


# vector3d = Vector3D(1, 2, 3)
# print(vector3d)

# vector3d_2 = Vector3D(1, 2, 3)
# print(vector3d_2)
# print(vector3d_2.get_memory_address())
