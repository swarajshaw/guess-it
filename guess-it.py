import random

real_number = random.randint(0,99)
# print(real_number)
guess_number = int(input("Enter the guess number between 0-99:\n"))

while True:
    if guess_number == real_number:
        print("Great guess you're correct")
        break

    elif guess_number < real_number:
        print("Your guess is low, please try again!")
        guess_number = int(input("Enter the guess number between 0-99:\n"))

    elif guess_number > real_number:
        print("Your guess is high, please try again!")
        guess_number = int(input("Enter the guess number between 0-99:\n"))
