#.Write a program to display the use of local, global and nonlocal variables

x = 100

def outer():
    y = 50  

    def inner():
        global x
        nonlocal y

        x = x + 10   
        y = y + 10   
        z = 20       

        print("Inside inner:")
        print("Global x =", x)
        print("Nonlocal y =", y)
        print("Local z =", z)

    inner()

    print("Inside outer:")
    print("Nonlocal y =", y)

outer()

print("Outside:")
print("Global x =", x)
