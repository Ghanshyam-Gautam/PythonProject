#There classes:
#Shape:
#has attribute color
#has method area, which prints "Let's calculate the area"
#Rectangle
#has attribute color,length and width
#has method area,which calculates the area and print:
#"let's calculate the area"
#The area of rectangle is {}*
#Circle
#has attribute color,radius
#has method area,which calculates the area and print:
#"let's calculate the area"
#The area of circle is {}*


class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        print("Let's calculate area")


class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def area(self):
        super().area()
        area = self.length * self.width
        print(f"The area of rectangle is {area}")


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        super().area()
        area = 3.14 * self.radius * self.radius
        print(f"The area of circle is {area}")


r1 = Rectangle('blue',7,9)
r1.area()

c1 = Circle('red', 2)
c1.area()
