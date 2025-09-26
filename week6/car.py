#create a car class with color attribute,write a method to change color

class car:
    def __init__(self,color):
        self.color=color

    def new_color(self,new_color):
        self.color=new_color

car1=car('red')

car1.new_color("orange")
print(car1.color)






