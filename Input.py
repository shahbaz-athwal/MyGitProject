from Calculator import add, subtract, multiply, divide


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


def execute_operation(choice, num1, num2):
    if choice == 1:
        return add(num1, num2)
    elif choice == 2:
        return subtract(num1, num2)
    elif choice == 3:
        return multiply(num1, num2)
    elif choice == 4:
        return divide(num1, num2)
    elif choice == 5:
        return exit()
