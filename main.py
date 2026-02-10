def greet_user():
    print("Welcome to the calculator!\n\n")


def take_input():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    return num1, num2


def show_menu():
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = int(input("\nEnter your choice: "))
    return choice
