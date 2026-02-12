from Input import greet_user, take_input, show_menu, execute_operation


def main():
    greet_user()
    num1, num2 = take_input()
    choice = show_menu()
    result = execute_operation(choice, num1, num2)
    print(f"The result is: {result}")


if __name__ == "__main__":
    main()
