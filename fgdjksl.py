from random import randint


class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def get_grade(self, grade: int):
        self.grades.append(grade)

    def get_random_grades(self):
        self.grades.append(randint(2, 5))


s1 = Student("Кирилл")
s2 = Student("Миша")
print(s1.name)
for i in range(7):
    s1.get_random_grades()
for i in range(7):
    s2.get_random_grades()

print(s1.name)
print(s1.grades)
print(s2.name)
print(s2.grades)

