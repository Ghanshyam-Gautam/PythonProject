# teacher has empty list and a student name on it

class Students:
    def __init__(self,name):
        self.name=name

class Teacher:
    def __init__(self,name):
        self.name=name
        self.students=[]

    def add_student(self,student):
        self.students.append(student)

    def showem(self):
        print(f"I am {self.name}")
        print("Here is my list of students: ")
        for student in self.students:
            print(student.name)

t1=Teacher("Ram")
t2=Teacher("Marry")

s1=Students("Bob")
s2=Students("John")
s3=Students("Alice")

t1.add_student(s1)
t1.add_student(s2)

t2.add_student(s2)
t2.add_student(s3)
t2.add_student(s1)

t1.showem()

t2.showem()

