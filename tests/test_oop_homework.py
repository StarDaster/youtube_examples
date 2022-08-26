from netology.homeworks.mentors_students import Lecturer, Student, Reviewer, avg_for_list_of_students


def test_rate_lecturer():
    lecturer = Lecturer(name="Nikolai", surname="Sviridov", courses_attached=["python", "git", "go"])
    student_1 = Student(name="Ivan", surname="Ivanov", gender="male")
    student_2 = Student(name="Petr", surname="Petrov", gender="male")
    student_3 = Student(name="Maria", surname="Sidorova", gender="female")
    student_1.rate_lecturer(lecturer=lecturer, course="python", grade=10)
    student_2.rate_lecturer(lecturer=lecturer, course="python", grade=10)
    student_3.rate_lecturer(lecturer=lecturer, course="git", grade=10)
    assert lecturer.grades == {
        "python": [10, 10],
        "git": [10],
        "go": []
    }


def test_avg_lecturer_course():
    lecturer = Lecturer(name="Nikolai", surname="Sviridov", courses_attached=["python", "git", "go"])
    student_1 = Student(name="Ivan", surname="Ivanov", gender="male")
    student_2 = Student(name="Petr", surname="Petrov", gender="male")
    student_3 = Student(name="Maria", surname="Sidorova", gender="female")
    student_1.rate_lecturer(lecturer=lecturer, course="python", grade=10)
    student_2.rate_lecturer(lecturer=lecturer, course="python", grade=10)
    student_3.rate_lecturer(lecturer=lecturer, course="git", grade=10)
    assert lecturer.avg_grade == 10


def test_avg_homework_rate():
    reviewer = Reviewer(name="Nikolai", surname="Sviridov")
    reviewer.add_course_to_attached("git")
    reviewer.add_course_to_attached("python")
    student = Student(name="Ivan", surname="Ivanov", gender="male")
    student.add_course_in_progress("git")
    student.add_course_in_progress("python")
    reviewer.rate_hw(student=student, course="git", grade=10)
    reviewer.rate_hw(student=student, course="python", grade=10)
    reviewer.rate_hw(student=student, course="git", grade=10)
    assert student.avg_homeworks == 10


def test_all_students_avg():
    reviewer = Reviewer(name="Nikolai", surname="Sviridov")
    reviewer.add_course_to_attached("python")

    student_1 = Student(name="Ivan", surname="Ivanov", gender="male")
    student_1.add_course_in_progress("python")

    student_2 = Student(name="Petr", surname="Petrov", gender="male")
    student_2.add_course_in_progress("python")

    student_3 = Student(name="Maria", surname="Sidorova", gender="female")
    student_3.add_course_in_progress("python")

    reviewer.rate_hw(student=student_1, course="python", grade=10)
    reviewer.rate_hw(student=student_2, course="python", grade=10)
    reviewer.rate_hw(student=student_3, course="python", grade=10)

    assert avg_for_list_of_students([student_1, student_2, student_3]) == 10
