# define the functions needed: add, sub, mul, div
# print options to the user
# ask for values
# call the functions
# while loop to continue the program until the user wants to exit

# ================================================================

def add(a, b):
    answer = a + b
    print(str(a)+ " + " + str(b) + " = " + str(answer))

def sub(a, b):
    answer = a - b
    print(str(a)+ " - " + str(b) + " = " + str(answer))

def mul(a, b):
    answer = a * b
    print(str(a)+ " * " + str(b) + " = " + str(answer))

def div(a, b):
    if b == 0:
        print("Error: Division by zero is not allowed.")
    else:
        answer = a / b
        print(str(a)+ " / " + str(b) + " = " + str(answer))

def main():
    while True:
        print("\nChoose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            add(a, b)
        elif choice == 2:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            sub(a, b)
        elif choice == 3:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            mul(a, b)
        elif choice == 4:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            div(a, b)
        elif choice == 5:
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
                main()
                main()


