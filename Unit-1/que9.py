#Write a program to create a function which accepts 2 numbers and one 
#arithmetic operator. Return the answer accordingly.
def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b if b != 0 else "Error"
    else:
        return "Invalid operator"

# User input
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

print("Result:", calculate(a, b, op))


