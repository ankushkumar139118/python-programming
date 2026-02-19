#Write a program to input 2 numbers and one arithmetic operator. Perform
#operations as per arithmetic operator which is given as input

x=int(input("enter a number in x :"))
y=int(input("enter a number in y :"))

op=input("select opereter ['add','sub','mul','div'] :")
result=0
if op=='add':
    result=x+y

elif op=='sub':
    result=x-y

elif op=='mul':
    result=x*y

elif op=='div':
    result=x/y
else:
    print("Invalid operator.....")
print(x, op, y, '=', result)
