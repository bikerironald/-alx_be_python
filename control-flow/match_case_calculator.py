# Simple Calculator with Match Case
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

def calculate(num1, num2, operation):
    match operation:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            if num2 == 0:
                return "Error: Division by zero"
            return num1 / num2
        case _:
            return "Error: Invalid operation"
result = calculate(num1, num2, operation)
print(f"The result of {num1} {operation} {num2} is: {result}")