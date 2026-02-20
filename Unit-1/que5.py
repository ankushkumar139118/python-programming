#Write a program to enter 10 numbers and display largest odd number
#from the entered number.
num1=int(input("enter the number 1:"))
num2=int(input("enter the number 2:"))
num3=int(input("enter the number 3:"))

if (num1>num2) and (num2>num3):
    print(num1, "is largest number:")
elif(num2>num1) and (num2>num3):
    print(num2, "is largest number:")
else:
    print(num3, "is largest number:")
    
    
