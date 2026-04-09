a=int(input("enter number 1:"))
b=int(input("enter number 2:"))
c=int(input("enter number 3:"))

def large(x,y,z):
    if(x>y and x>z):
        print(f"{x} is greart than {y}  and {z}")
    elif(y>x and y>z):
        print(f"{y} is greart than {x} and {z}")
    else:
        print(f"{z} is greart than {x} and {y}")
large(a,b,c)
