class Vector2D:
    def __init__(self, coord_x: float, coord_y: float):
        self.coord_x = coord_x
        self.coord_y = coord_y

    def __add__(self, other: 'Vector2D'):
        result_x = self.coord_x + other.coord_x
        result_y = self.coord_y + other.coord_y
        return Vector2D(coord_x=result_x, coord_y=result_y)

    def __str__(self):
        return f"Вектор с координатами\n" \
               f"x: {self.coord_x}\n" \
               f"y: {self.coord_y}\n"

    def some_method(self):
        return 678

    def some_other_method(self):
        return f"{self} ХАХАХАХА"


class MixinFirst:
    def some_method(self):
        return 123


class MixinSecond:
    def some_method(self):
        return 1230000


class Vector3D(MixinFirst, Vector2D, MixinSecond):
    def __init__(self, coord_x: float, coord_y: float, coord_z: float):
        super().__init__(coord_x=coord_x, coord_y=coord_y)
        self.coord_z = coord_z

    def __add__(self, other: 'Vector3D'):
        result_x = self.coord_x + other.coord_x
        result_y = self.coord_y + other.coord_y
        result_z = self.coord_z + other.coord_z
        return Vector3D(coord_x=result_x, coord_y=result_y, coord_z=result_z)

    def __str__(self):
        res_str = super().__str__()
        return res_str + f"z: {self.coord_z}"

    def some_method(self):
        return super(Vector2D, self).some_method()


vector_3d = Vector3D(1, 2, 3)
# vector_3d_2 = Vector3D(2, 3, 4)
# print(vector_3d_2 + vector_3d)
print(vector_3d.some_method())
