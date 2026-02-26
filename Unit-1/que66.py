#Define a procedure histogram() that takes a list of integers and prints a
# histogram to the screen. For example, histogram([4, 9, 7]) should print
# the following:
# ****
# *********
# *******
def histogram(numbers):
    for i in numbers:
        print(i * '*')

numbers = []

x = int(input("Enter the list length: "))
print("Enter", x, "integers:")

for i in range(x):
    data = int(input())
    numbers.append(data)

histogram(numbers)