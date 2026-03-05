#Write a program to generate arithmetic exception and log the exception in system.
#import logging

logging.basicConfig(filename="error.txt", level=logging.ERROR)

try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    c = a / b
    print("Result:", c)

except ZeroDivisionError as e:
    print("Error: Cannot divide by zero")
    logging.error(e)

print("Program Ended")
