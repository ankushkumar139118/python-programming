#Write a program to enter 10 numbers and display all armstrong numbers
#from those numbers
number=int(input("enter a number here :"))

sum=0
temp = number

while temp > 0:
    digit = temp%10
    sum += digit ** 3
    temp //=10

if sum == number:
    print('it is a armstrong number')

else:
    
    print("it is not an armstrong number")
    

