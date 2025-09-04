inch = float(input("Enter inch "))
while inch >= 0:
    cm = inch * 2.54
    print(f"{inch} is equal to {cm:.2f} centimeter")
    inch = float(input("Enter inch "))
print("program end")