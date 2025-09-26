

class student:
    def __init__(self,name):
     self.name=name

    def introduce(self):
        print(f"Hi, I'm {self.name} ")

p1=student("Alice")
p2=student("Bob")
p3=student("Jack")

p1.introduce()
p2.introduce()
p3.introduce()