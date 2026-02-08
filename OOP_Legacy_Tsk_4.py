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

# Функции для подсчета средних оценок
def avg_grade_students(students_list, course_name):
    all_grades = []
    for student in students_list:
        if course_name in student.grades:
            all_grades.extend(student.grades[course_name])
    if not all_grades:
        return 0
    return round(sum(all_grades) / len(all_grades), 1)

def avg_grade_lecturers(lecturers_list, course_name):
    all_grades = []
    for lecturer in lecturers_list:
        if course_name in lecturer.grades:
            all_grades.extend(lecturer.grades[course_name])
    if not all_grades:
        return 0
    return round(sum(all_grades) / len(all_grades), 1)

# --- Пример использования по всем критериям ---

# Создаем по 2 экземпляра
l1, l2 = Lecturer('Иван', 'Иванов'), Lecturer('Петр', 'Петров')
r1, r2 = Reviewer('Сидор', 'Сидоров'), Reviewer('Вася', 'Пупкин')
s1, s2 = Student('Ольга', 'Алёхина', 'Ж'), Student('Коля', 'Николаев', 'М')

# Настраиваем курсы
l1.courses_attached += ['Python']
l2.courses_attached += ['Python']
r1.courses_attached += ['Python']
s1.courses_in_progress += ['Python']
s2.courses_in_progress += ['Python']

# Вызываем методы
r1.rate_hw(s1, 'Python', 10)
r1.rate_hw(s2, 'Python', 8)
s1.rate_lecture(l1, 'Python', 10)
s2.rate_lecture(l1, 'Python', 8)

# Проверка функций
print(f"Средняя по студентам (Python): {avg_grade_students([s1, s2], 'Python')}")
print(f"Средняя по лекторам (Python): {avg_grade_lecturers([l1, l2], 'Python')}")

# Проверка сравнения
print(f"Студент 1 > Студент 2: {s1 > s2}")