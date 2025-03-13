# This is a simple calculator that can add, subtract, multiply, or divide two numbers.
def calculator():
    while True:
        print("Calculator Options:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Choose operation (1-5): ")

        if choice == '5':
            print("Goodbye!")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Wrong choice! Please select a valid option.")
            continue

        num1_input = input("Enter first number: ")
        num2_input = input("Enter second number: ")

        if not (num1_input.isnumeric() and num2_input.isnumeric()):
            print("Oops! That doesn't seem to be a valid number. Try again!")
            continue

        num1 = float(num1_input)
        num2 = float(num2_input)

        if choice == '1':
            print(f"{num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            print(f"{num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print(f"{num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            if num2 == 0:
                print("Can't divide by zero!")
            else:
                print(f"{num1} / {num2} = {num1 / num2}")

        again = input("Another calculation? (yes/no): ")
        if again.lower() != 'yes':
            print("Thanks for using the calculator. Bye!")
            break

calculator()
