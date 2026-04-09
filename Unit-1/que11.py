#Write a program to create function which shall accept any number of 
#arguments and display total of all the numbers given as argument.
n = int(input("How many numbers you want to enter: "))

numbers = []
def total_sum(*args):
    total = 0
    for num in args:
        total += num
    return total

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

result = total_sum(*numbers)

print("Total =", result)
