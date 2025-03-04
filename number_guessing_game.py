import random

def main():
    print("Welcome to the Infinite Number Guessing Game!")
    print("I'll keep thinking of numbers until you quit or fail.")

    while True:
        print("\nNew Round!")
        print("I'm thinking of a number between 1 and 100.")
        
        number = random.randint(1, 100)
        number_of_attempts = 0

        while number_of_attempts < 11:
            user_input = input("Enter your guess (or 'quit' to stop playing): ")
            
            if user_input.lower() == 'quit':
                print("Thanks for playing!")
                return
            
            try:
                number_guessed = int(user_input)
            except ValueError:
                print("Invalid input. Please enter a number or type 'quit'.")
                continue
            
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

if __name__ == "__main__":
    main()
