num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2 if num2 != 0 else "Error: Divide by zero"

# you can add more operations here like exponentiation, modulus, etc.
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

result = operations.get(operator, lambda x, y: "Invalid operator")(num1, num2)

print("Result: ", result)
