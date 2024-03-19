# Simple Arithmetic Calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero! Result of a division by zero is undefined" 
    else:
        return x / y

def mod(x, y):
    if y == 0:
        return "Error: Modulo by zero! Result of a modulo by zero is undefined" 
    else:
        return x % y

def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def get_operation():
    while True:
        print("Welcome to Simple Calculator!")
        operation = input("Choose operation (+, -, *, /, %) or type 'exit' to quit: ")
        if operation.lower() in ['+', '-', '*', '/', '%']:
            return operation
        elif operation.lower() == 'exit':
            return 'exit'
        else:
            print("Invalid operation! Please choose from '+', '-', '*', '/', '%'.")

def calculator():
    while True:
        operation = get_operation()
        if operation == 'exit':
            print("Exiting calculator.")
            print("Thank You!.")
            break

        num1 = get_number_input("Enter first number: ")
        num2 = get_number_input("Enter second number: ")

        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        elif operation == '%':
            result = mod(num1, num2)

        print("Result:", result)

        choice = input("Do you want to continue? (yes/no): ")
        if choice.lower() != 'yes':
            print("Exiting calculator.")
            break

if __name__ == "__main__":
    calculator()
