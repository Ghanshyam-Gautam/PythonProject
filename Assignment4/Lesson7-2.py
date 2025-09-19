# Initialize an empty tuple to store names
names = ()

while True:
    # Ask the user to enter a name
    name = input("Enter a name: ")

    if name == "":
        break

    if name in names:
        print("Existing name")
    else:
        print("New name")
        names += (name,)  # Add the new name by creating a new tuple

print("\nList of entered names:")
for name in names:
    print(name)