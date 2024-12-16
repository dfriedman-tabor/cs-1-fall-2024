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


# test our student code

jace = Student("Jace", 12, "Tabor", 2.8)
will = Student("Will", 11, "Tabor", 4.5)

jace.takeTest(.4)

print(will)



class Class:

    def __init__(self, title, teacher, roster):
        self.title= title
        self.teacher = teacher
        self.roster = roster

    def __str__(self):
        return self.title + ", taught by " + self.teacher + ", with " + str(len(self.roster)) + " students"

    def averageGPA(self):
        total = 0
        for i in range(len(self.roster)):
            total += self.roster[i].gpa
        print(total/len(self.roster))

    def findStudent(self, target):
        for i in range(len(self.roster)):
            if target in self.roster[i].name:
                print(self.roster[i])


# test our classroom code
cs2 = Class("CS 2", "friedman", [Student("Will", 11,"Tabor",4.5), Student("Jace", 12, "Tabor",2.1), Student("Renad", 11, "Tabor", 3.4)])

print(cs2)






