#Write a program to create a list and perform various operations on list using menu
#my_list = []

while True:
    print("\n--- LIST MENU ---")
    print("1. Create List")
    print("2. Display List")
    print("3. Add Element")
    print("4. Remove Element")
    print("5. Search Element")
    print("6. Sort List")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        my_list = list(map(int, input("Enter elements (space separated): ").split()))
        print("List created successfully!")

    elif choice == 2:
        print("Current List:", my_list)

    elif choice == 3:
        elem = int(input("Enter element to add: "))
        my_list.append(elem)
        print("Element added!")

    elif choice == 4:
        elem = int(input("Enter element to remove: "))
        if elem in my_list:
            my_list.remove(elem)
            print("Element removed!")
        else:
            print("Element not found!")

    elif choice == 5:
        elem = int(input("Enter element to search: "))
        if elem in my_list:
            print("Element found at index:", my_list.index(elem))
        else:
            print("Element not found!")

    elif choice == 6:
        my_list.sort()
        print("List sorted!")

    elif choice == 7:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
