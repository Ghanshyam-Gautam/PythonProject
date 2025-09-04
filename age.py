age = int(input("Enter your age: "))
if age<= 5:
    print("ticket is free.")
elif 5 <=age < 17:
    print("ticket is $7.")
elif 18 <= age < 59:
    print("ticket is $12")
else:
    print("free ticket.")

