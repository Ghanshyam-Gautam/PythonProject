import random

# 🎲 Function to simulate a dice roll with a given number of sides
def roll_dice(sides):
    return random.randint(1, sides)

# Ask the user for the number of sides
sides = int(input("Enter the number of sides on the dice: "))

# Roll until we hit the maximum number
result = 0
while result != sides:
    result = roll_dice(sides)
    print(f"Rolled: {result}")