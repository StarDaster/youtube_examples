class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    @staticmethod
    def rate_lecturer(lecturer: 'Lecturer', course: str, grade: int):
        lecturer.grades[course].append(grade)

    def __str__(self):
        return f"Имя: {self.name}\nSurname: {self.surname}\n" \
               f"Средняя оценка за домашние задания: {self.avg_homeworks}\n" \
               f"Курсы в процессе изучения: {'.'.join(self.courses_in_progress)}\n" \
               f"Завершенные курсы: {'.'.join(self.finished_courses)}"

    @property
    def avg_homeworks(self):
        hw_cnt = 0
        total = 0
        for course_grades in self.grades.values():
            total += sum(course_grades)
            hw_cnt += len(course_grades)
        if hw_cnt == 0:
            return 0
        return total / hw_cnt

    def add_course_in_progress(self, course: str):
        if course not in self.courses_in_progress:
            self.courses_in_progress.append(course)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def add_course_to_attached(self, course: str):
        if course not in self.courses_attached:
            self.courses_attached.append(course)


class Lecturer(Mentor):
    def __init__(self, name, surname, courses_attached):
        self.grades = {course: [] for course in courses_attached}
        super().__init__(name=name, surname=surname)

    def __str__(self):
        return f"Имя: {self.name}\nSurname: {self.surname}\nСредняя оценка за лекции: {self.avg_grade}"

    @property
    def avg_grade(self):
        courses_cnt = len(self.grades)
        total = 0
        for course in self.grades:
            total += sum(self.grades[course])
        return total / courses_cnt


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nSurname: {self.surname}"


def avg_for_list_of_students(student_list: list[Student]):
    return sum([student.avg_homeworks for student in student_list]) / len(student_list)
