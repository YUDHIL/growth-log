# import random and pick a secret number between 1 and 100
import random

secret_number = random.randint(1, 100)
print(secret_number)

# set attempts counter to 0
attempts = 0

# start a loop to ask the user for the guess
while True:
    try:
        guess = int(input("Enter your guess between 1 and 100:\n"))
    except ValueError:
        print("Invalid input,Please enter a valid number ")
        continue
    
    attempts += 1
    if guess > secret_number:
        print("Too high ! try again.")
    elif guess < secret_number:
        print("your guess is too low, try again.")
    else:
        print(f"Congratulation ! you guessed the number in {attempts} attempts.")
        break



