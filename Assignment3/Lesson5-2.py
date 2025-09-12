numbers = []

print("Enter numbers. Press Enter without typing anything to quit.")

while True:
    entry = input("Number: ")
    if entry == "":
        break
    if entry.isdigit():
        numbers.append(int(entry))
    else:
        print("Please enter a valid number.")

# Sort the numbers in descending order
numbers.sort(reverse=True)

# Print the top five greatest numbers
print("Top five greatest numbers in descending order :")
for num in numbers[:5]:
    print(num)