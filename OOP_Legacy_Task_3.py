class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def _get_avg_grade(self):
        if not self.grades:
            return 0
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        return sum(all_grades) / len(all_grades)

    def rate_lecture(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and
                course in lecturer.courses_attached and
                course in self.courses_in_progress and
                1 <= grade <= 10):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = (f"Имя: {self.name}\n"
               f"Фамилия: {self.surname}\n"
               f"Средняя оценка за домашние задания: {round(self._get_avg_grade(), 1)}\n"
               f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
               f"Завершенные курсы: {', '.join(self.finished_courses)}")
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            return "Ошибка"
        return self._get_avg_grade() < other._get_avg_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return self._get_avg_grade() == other._get_avg_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _get_avg_grade(self):
        if not self.grades:
            return 0
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        return sum(all_grades) / len(all_grades)

    def __str__(self):
        res = (f"Имя: {self.name}\n"
               f"Фамилия: {self.surname}\n"
               f"Средняя оценка за лекции: {round(self._get_avg_grade(), 1)}")
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return "Ошибка"
        return self._get_avg_grade() < other._get_avg_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return False
        return self._get_avg_grade() == other._get_avg_grade()

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
        return f"Имя: {self.name}\nФамилия: {self.surname}"

# Блок проверки

some_reviewer = Reviewer('Some', 'Buddy')
print(some_reviewer)
print()

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']

some_lecturer.grades = {'Python': [10, 10, 10, 10, 9]}
print(some_lecturer)
print()

some_student = Student('Ruoy', 'Eman', 'M')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в программирование']
some_student.grades = {'Python': [10, 9, 10, 10, 10], 'Git': [10]}
print(some_student)