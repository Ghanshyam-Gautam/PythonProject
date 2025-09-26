#class Student that has attribute name
#class Teacher that has attribute name
#for Teacher class, define a method "teaches",It takes a student
#it prints"name of the teacher" teaches "name of the student"

class Student:
    def __init__(self,name):
        self.name=name

class Teacher:
    def __init__(self,name):
        self.name=name

    def teaches(self,student):
        print(f"{self.name} teaches {student.name}")

s1=Student("Ram")
t1=Teacher("Hari")

t1.teaches(s1)