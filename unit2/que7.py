# Student Result System

def enter_marks():
    marks = []
    for i in range(1, 6):
        mark = float(input(f"Enter marks for subject {i}: "))
        marks.append(mark)
    return marks

def calculate_percentage(marks):
    total = sum(marks)
    percentage = total / len(marks)
    return percentage

def assign_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"

marks = []

while True:
    print("\n----- Student Result System -----")
    print("1. Enter Marks")
    print("2. Calculate Percentage")
    print("3. Assign Grade")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        marks = enter_marks()
        print("Marks entered successfully!")
        
    elif choice == 2:
        if marks:
            percentage = calculate_percentage(marks)
            print("Percentage:", percentage)
        else:
            print("Please enter marks first!")
            
    elif choice == 3:
        if marks:
            percentage = calculate_percentage(marks)
            grade = assign_grade(percentage)
            print("Grade:", grade)
        else:
            print("Please enter marks first!")
            
    elif choice == 4:
        print("Exiting program...")
        break
        
    else:
        print("Invalid choice! Please try again.")
