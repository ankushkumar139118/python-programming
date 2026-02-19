#Write a program to enter marks of 4 subjects and display result (result
#shall include total, percentage and grade)
num1=int(input("enter marks of subject mats:"))
num2=int(input("enter marks of subject english:"))
num3=int(input("enter marks of subject sanskrit:"))
num4=int(input("enter marks of subject scince:"))
num5=int(input("enter marks of subject socal scince:"))

total=num1+num2+num3+num4+num5
percentage = total/5

if percentage >=90:
    grade = "A+"
elif percentage >=75:
    grade = "A"
elif percentage >60:
      grade = "B"
elif percentage >45:
    grade = "C"
elif percentage>30:
    grade = "pass"
else:
    grade = "fail"
print("Total marks is :",total)
print("Percentage is :",percentage)
print("Grade is :",grade)
