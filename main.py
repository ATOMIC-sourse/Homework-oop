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

first_student = Student('Evan', 'Hill')
first_student.finished_courses = ['Ruby']
first_student.courses_in_progress = ['Python']

second_student = Student('Eva', 'Adam')
second_student.finished_courses = ['C++']
second_student.courses_in_progress = ['Python', 'Ruby']

first_mentor = Mentor('Jonh', 'Jones')
first_mentor.courses_attached = ['Python']

second_mentor = Mentor('Wendy', 'Davis')
second_mentor.courses_attached = ['Python' ,'Ruby']

first_lecturer = Lecturer('Jonh', 'Jones')
first_mentor.courses_attached = ['Python']

second_lecturer = Lecturer('Wendy', 'Davis')

first_reviewer = Reviewer('Jonh', 'Jones')
second_reviewer = Reviewer('Wendy', 'Jones')

first_student.rate_hw(first_lecturer, 'Python', 8)
first_student.rate_hw(first_lecturer, 'Python', 10)
second_student.rate_hw(second_lecturer, 'Python', 7)
second_student.rate_hw(second_lecturer, 'Ruby', 5)

first_reviewer.rate_hw(first_student, 'Python', 6)
first_reviewer.rate_hw(first_student, 'Python', 10)

second_reviewer.rate_hw(second_student, 'Python', 3)
second_reviewer.rate_hw(second_student, 'Python', 7)
second_reviewer.rate_hw(second_student, 'Ruby', 10)
second_reviewer.rate_hw(second_student, 'Ruby', 6)

# print(first_student)
# print(second_student)
# print(first_student == second_student)
#
# print(first_lecturer)
# print(second_lecturer)
# print(first_lecturer == second_lecturer)
# print(first_lecturer)
# print(first_student.courses_in_progress)

def ave():
    first = 0
    second = 0
    for i in first_student.average_grades():
        first += i
    for i in second_student.average_grades():
        second += i
    return (first + second) / 2

def ave1():
    first = 0
    second = 0
    for i in first_lecturer.average_grades():
        first += i
    for i in second_lecturer.average_grades():
        second += i
    return (first + second) / 2