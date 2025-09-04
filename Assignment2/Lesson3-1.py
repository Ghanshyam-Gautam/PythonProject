length = int(input("Enter the length of Zander in centimeters "))
if length < 42:
    difference= 42-length
    print("Release the fish back into the lake")
    print(f"The fish is {difference} cm below the size limit.")
else:
    print("You can keep it")

