# Banking System

balance = 0   # Global balance

# Function to Deposit Money
def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        print("Amount deposited successfully!")
    else:
        print("Invalid amount!")

# Function to Withdraw Money
def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if amount <= balance and amount > 0:
        balance -= amount
        print("Amount withdrawn successfully!")
    else:
        print("Insufficient balance or invalid amount!")

# Function to Check Balance
def check_balance():
    print("Current Balance:", balance)


# Menu Driven Program
while True:
    print("\n----- Banking System -----")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        deposit()
        
    elif choice == 2:
        withdraw()
        
    elif choice == 3:
        check_balance()
        
    elif choice == 4:
        print("Thank you for using Banking System!")
        break
        
    else:
        print("Invalid choice! Please try again.")
