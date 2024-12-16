import random


class Student:

    def __init__(self, name, grade, school, gpa):
        self.name = name
        self.grade = grade
        self.school = school
        self.gpa = gpa

    def __str__(self):
        return self.name + ", at " + self.school + ", gpa: " + str(self.gpa)

    def takeTest(self, difficulty):
        if random.random() > difficulty:
            self.gpa += .1
        else:
            self.gpa -= .1


jace = Student("Jace", 12, "Tabor", 2.8)
will = Student("Will", 11, "Tabor", 4.5)

jace.takeTest(.4)

print(will)






