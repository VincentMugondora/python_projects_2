# Number Guessing Game:

# The computer selects a random number, and the user tries to guess it with hints (e.g., higher or lower).

# Skills: Random module, loops

import random

def main():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number = random.randint(1, 100)
    number_of_attempts = 0

    while number_of_attempts < 11:
        number_guessed = int(input("Enter your guess: "))
        number_of_attempts += 1

        if number_guessed < number:
            print("Too low! Try again.")
        elif number_guessed > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {number_of_attempts} attempts.")
            break

        if number_of_attempts == 11:
            print("Sorry, you didn't guess the number.")
            print(f"The number was {number}.")
            break
        return number_of_attempts

main()