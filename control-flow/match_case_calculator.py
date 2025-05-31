# num1 = input("Enter the first number: ")
# num2 = input("Enter the second number: ")
# operation = input("Enter the operation (+, -, *, /): ")
# def calculate(num1, num2, operation):
#     match operation:
#         case '+':
#            print("num1+num2")
#         case '-':
#             print("num1-num2")
#         case '*':
#             print("num1*num2")
#         case '/':
#             print("num1/num2")
# result = calculate((num1), (num2), operation)
# print(f"The result is: {result}")


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
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
            if num2 != 0:
                return num1 / num2
            else:
                return "Error: Division by zero"
        case _:
            return "Invalid operation"

result = calculate(num1, num2, operation)
print(f"The result is: {result}")