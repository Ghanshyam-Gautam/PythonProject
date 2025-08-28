import random

digit1 = random.randint(0, 9)
digit2 = random.randint(0, 9)
digit3 = random.randint(0, 9)

roll1 = random.randint(1, 6)
roll2 = random.randint(1, 6)
roll3 = random.randint(1, 6)
roll4 = random.randint(1, 6)


print("Random combination lock codes:")
print(f"3-digit code (0–9): {digit1}-{digit2}-{digit3}")
print(f"4-digit code (1–6): {roll1}-{roll2}-{roll3}-{roll4}")