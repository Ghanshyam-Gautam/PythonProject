# create a class Person with a name,
# create a subclass of Person, which is a Teacher
# a person has a name
#a teacher has also a name
#In addition, the teacher has a method called"teach",which prints:"Teacher {} is teaching"

class Person:
    def __init__(self,name):
        self.name=name

class Teacher(Person):
    def __int__(self,name):
        super.__init__(name)

    def teaches(self):
        print(f"{self.name} is now teaching")

t1=Teacher("Bob")
t2=Teacher("Alice")
t3=Teacher("George")

t2.teaches()

