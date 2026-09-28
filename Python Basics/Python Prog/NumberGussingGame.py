import random

number = random.randint(1,100)
attempts = 0

while True:
    Choice = int(input(" Enter the Number :"))
    attempts += 1

    if Choice == number:
        print("Congrats.... your guess is correct")
        break

    elif Choice < number:
        print(" too low number...")

    else:
        print(" Too higher Number...")
