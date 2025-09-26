

class person:
    def __init__(self,name,age):
     self.name=name
     self.age=age

    def showinfo(self):
        print(f"My name is {self.name} and I am {self.age} years old")

p1=person("Alice","21")
p2=person("Bob","22")
p3=person("Jack","23")

p1.showinfo()
p2.showinfo()
p3.showinfo()