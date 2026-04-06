#Write a Python program to perform following operation on given string input:
#a) Count Number of Vowel in given string
#b) Count Length of string (donot use len() )
#c) Reverse string
#d) Find and replace operation
#e) check whether string entered is a palindrome or not
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count

def string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count
def reverse_string(s):
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev
def find_replace(s):
    find_word = input("Enter word to find: ")
    replace_word = input("Enter word to replace with: ")
    return s.replace(find_word, replace_word)

def is_palindrome(s):
    start = 0
    end = string_length(s) - 1
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True
text = input("Enter a string: ")

while True:
    print("\nMenu:")
    print("1. Count vowels")
    print("2. Find length")
    print("3. Reverse string")
    print("4. Find and replace")
    print("5. Check palindrome")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        print("Number of vowels:", count_vowels(text))

    elif choice == '2':
        print("Length of string:", string_length(text))

    elif choice == '3':
        print("Reversed string:", reverse_string(text))

    elif choice == '4':
        text = find_replace(text)
        print("Updated string:", text)

    elif choice == '5':
        if is_palindrome(text):
            print("The string is a palindrome.")
        else:
            print("The string is not a palindrome.")

    elif choice == '6':
        print("Exiting program.")
        break

    else:
        print("Invalid choice! Please try again.")
