# # class Matr:
# #     def __init__(self, color):
# #         self.color = color
# #
# #
# # matr_1 = Matr(color="red")
# # matr_2 = Matr(color="blue")
# #
# # print(matr_1)
# # print(matr_2)
# from math import sqrt
#
#
# class Advertizer:
#     @staticmethod
#     def show_adv():
#         print(f"Реклама: покупайте наших котят!")
#
#
# class Vector2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"x: {self.x}\ny: {self.y}"
#
#     @property
#     def module(self):
#         return (self.x ** 2 + self.y ** 2) ** 0.5
#
#     def __eq__(self, other):
#         mod_1 = self.module
#         mod_2 = other.module
#         return mod_1 == mod_2
#
#     def __lt__(self, other):
#         mod_1 = (self.x ** 2 + self.y ** 2) ** 0.5
#         mod_2 = (other.x ** 2 + other.y ** 2) ** 0.5
#         return mod_1 < mod_2
#
#     # ne, gt, ge, le
#
#
# class Vector3D(Vector2D, Advertizer):
#     def __init__(self, x, y, z):
#         super().__init__(x=x, y=y)
#         self.z = z
#
#     def __str__(self):
#         self.show_adv()
#         res = super().__str__()
#         return f"{res}\nz: {self.z}"
#
#
# vect_2d_1 = Vector2D(x=0, y=1)
# vect_2d_2 = Vector2D(x=0, y=2)
#
# print(vect_2d_1)
# print(vect_2d_1 < vect_2d_2)

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
                c = 1
            else:
                student.grades[course] = [grade]
                c = 1
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)