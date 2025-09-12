import random
secret_number=random.randint(1,10)
print("Guess the number between 1 to 10")
while True:
    guess=int(input("Guess the number: "))
    if guess<secret_number:
        print("too low")
    elif guess>secret_number:
        print("too high")
    else:
        print("Correct")
    break
