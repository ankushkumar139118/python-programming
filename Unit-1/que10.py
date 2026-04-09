#Write a program to create 4 lambda functions which shall accept 2 
#numbers and one arithmetic operator. As per arithmetic operator related 
#lambda functions Shall be invoked.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

print("Result =", calculate(a, b, op))

def calculate(a, b, op):
    if op == '+':
        return add(a, b)
    elif op == '-':
        return sub(a, b)
    elif op == '*':
        return mul(a, b)
    elif op == '/':
        return div(a, b)
    else:
        return "Invalid operator"
    
add = lambda x, y: x + y
sub = lambda x, y: x - y
mul = lambda x, y: x * y
div = lambda x, y: x / y if y != 0 else "Error: Division by zero"
