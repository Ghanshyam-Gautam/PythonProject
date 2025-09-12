import random

num_dice = int(input("How many dice would you like to roll? "))

total = 0

# Roll each die and add to the total
for i in range(num_dice):
    roll = random.randint(1, 6)
    print(f"Die {i+1}: {roll}")
    total += roll

# Print the final sum
print(f"Total sum of all dice: {total}")