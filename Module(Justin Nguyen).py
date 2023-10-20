
# 1a) Has a function to calculate the square footage of a house
# Reminder of Formula: Length X Width == Area

import math

def calculate_square_footage():
    try:
        length = float(input("Enter the length of the house (in feet): "))
        width = float(input("Enter the width of the house (in feet): "))
        area = length * width
        return area
    except ValueError:
        print("Invalid input. Please enter a number.")
        return calculate_square_footage()

square_footage = calculate_square_footage()

if square_footage is not None:
    print(f"The square footage of the house is {square_footage} square feet.")


# 1b) Has a function to calculate the circumference of a circle 2 Pi r
# import math

def calculate_circumference():
    while True:
        try:
            radius = float(input("Please enter the radius of the circle: "))
            if radius < 0:
                print("Radius cannot be negative. Please try again.")
                continue
            circumference = 2 * math.pi * radius
            print(f"The circumference of the circle is {circumference:.2f} units.")
            break
        except ValueError:
            print("Invalid input. Please re-enter the radius.")

calculate_circumference()

# 2) Build a Shopping Cart Function
# You can use either lists or dictionaries. The program should have the following capabilities:

# 1) Takes in input
# 2) Stores user input into a dictionary or list
# 3) The User can add or delete items
# 4) The User can see current shopping list
# 5) The program Loops until user 'quits'
# 6) Upon quiting the program, print out all items in the user's list

# Ask the user four bits of input: Do you want to : Show/Add/Delete or Quit?
# Initial empty list to store shopping items
shopping_list = []

while True:
    print("\nOptions:")
    print("1. Add item(s)")
    print("2. Remove item(s)")
    print("3. Show shopping cart")
    print("4. Quit")

    choice = input("Enter your choice (select #): ")

    if choice == '1':
        item = input("Enter the item you would like to add: ")
        shopping_list.append(item)

    elif choice == '2':
        item = input("Enter the item you would like to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
        else:
            print("Item was not found in shopping cart.")

    elif choice == '3':
        print("\nShopping Cart:")
        for i, item in enumerate(shopping_list):
            print(f"{i+1}. {item}")

    elif choice == '4':
        print("Quitting ...")
        break

    else:
        print("Invalid choice. Please try again.")