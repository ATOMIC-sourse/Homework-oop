class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grades()

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def average_grades(self):
        avr_grades = 0
        count = 0
        for grades in self.grades.values():
            for grade in grades:
                avr_grades += grade
                count += 1
            return avr_grades / count

    def __str__(self):
        return f'Имя: {self.name}\n'\
                f'Фамилия: {self.surname}\n'\
                f'Средняя оценка за домашние задания: {self.average_grades()}\n'\
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'\
                f'Завершенные курсы: {", ".join(self.finished_courses)}'

    def __eq__(self, other):
        return isinstance(other, Student) and self.average_grades() == other.average_grades()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grades(self):
        avr_grades = 0
        count = 0
        for grades in self.grades.values():
            for grade in grades:
                avr_grades += grade
                count += 1
            return avr_grades / count

    def __str__(self):
        return f'Имя: {self.name}\n'f'Фамилия: {self.surname}'

    def __eq__(self, other):
        return isinstance(other, Lecturer) and self.average_grades() == other.average_grades()


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
        return f'Имя: {self.name}\n'f'Фамилия: {self.surname}\n'





some_student = Student('Ruoy', 'Eman')
some_student1 = Student('Gaibe', 'Name')


some_student.courses_in_progress += ['Python']
some_student1.courses_in_progress += ['C++']


some_student.finished_courses += ["C++"]
some_student.finished_courses += ["Java"]

some_lecturer1 = Lecturer("Go", "Ahead")

some_lecturer = Lecturer("Some", "Buddy")

some_lecturer.courses_attached = ['Python']
some_lecturer1.courses_attached = ['C++']

some_student.rate_hw(some_lecturer, 'Python', 10)
some_student.rate_hw(some_lecturer1, 'C++', 10)

some_reviewer = Reviewer("Some", "Buddy")
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['C++']


some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student1, 'C++', 5)
# print(some_lecturer)
# print(some_reviewer)
# print(some_student)
