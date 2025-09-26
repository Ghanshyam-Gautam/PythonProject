#write a rectangle class with width and height.Add method
#"area " and "perimeter" to compute area and perimeter

class rectangle:
    def __init__(self,height,width):
        self.height=height
        self.width=width

    def area (self):
        return (self.height*self.width)

    def perimeter(self):
        return 2*(self.height + self.width)

r1=rectangle(4,6 )


print(f"the area is {r1.area()}")
print(f"the perimeter is {r1.perimeter()}")

