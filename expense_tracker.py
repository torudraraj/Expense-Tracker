"""
===============================================================================
ENGR 13300 Fall 2023

Program Description
    This program is for the user to keep their own personal expense tracker file.

Assignment Information
    Assignment:     Ind Final Project
    Author:         Rudra Raj, raj48@purdue.edu
    Team ID:        LC1 - 10 (e.g. LC1 - 01; for section LC1, team 01)

Contributor:    Name, login@purdue [repeat for each]
    My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.
    
ACADEMIC INTEGRITY STATEMENT
I have not used source code obtained from any other unauthorized
source, either modified or unmodified. Neither have I provided
access to my code to another. The project I am submitting
is my own original work.
===============================================================================
"""

from expense_functions import *

# Variables to store user expenses, password, and budget
expenses = []
password = None
budget = 0.0

def register_user():
    global password
    new_password = input("Set your new password: ")
    
    if password is not None and new_password == password:
        print("New password is the same as the old one. You can use it.")
    else:
        password = new_password
        print("Registration successful!\n")

    return True  # Return True to indicate successful registration

def authenticate_user():
    global password
    entered_password = input("Enter your password: ")
    attempts = 1

    while entered_password != password and attempts < 3:
        print(f"\nAuthentication failed. Please try again. Attempts remaining: {3 - attempts}\n")
        entered_password = input("Enter your password: ")
        attempts += 1

    if entered_password == password:
        return True
    else:
        print("Too many unsuccessful attempts. Exiting...")
        return False

def reset_password():
    global password
    new_password = input("Enter your new password: ")
    password = new_password
    print("Password reset successful. You can now log in with your new password.")

def get_expense_details():
    while True:
        try:
            date_str = input("Enter the date (MM-DD-YYYY): ")
            date = datetime.strptime(date_str, "%m-%d-%Y").strftime("%m-%d-%Y")
            break
        except ValueError:
            print("Invalid date format. Please enter the date in MM-DD-YYYY format.")

    while True:
        print("Expense Types:")
        for i, expense_type in enumerate(expense_types, start=1):
            print(f"{i}. {expense_type}")

        try:
            category_index = int(input("Enter the number corresponding to the expense type: "))
            if 1 <= category_index <= len(expense_types):
                category = expense_types[category_index - 1]
                break
            else:
                print("Invalid expense type. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    amount = None
    while amount is None:
        try:
            amount = float(input("Enter the amount spent: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")

    # Check if the expense exceeds the budget
    if budget > 0 and amount > budget:
        print("Error: Expense exceeds the budget. Please enter a valid amount.")
        return None

    return date, category, amount

def main():
    global expenses, budget, password

    registered = False

    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        initial_choice = input("Enter your choice: ")

        if initial_choice == "1":
            if register_user():
                print("Returning to login page...\n")
            else:
                print("Registration failed. Please try again.\n")
            registered = True

        elif initial_choice == "2":
            if authenticate_user():
                registered = True
                break
            else:
                print("Authentication failed. Please try again.")
        elif initial_choice == "3":
            print("Exiting the Expense Tracker...")
            break
        else:
            print("Invalid choice. Please try again.")

    while registered:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. Total Expenses (Category)")
        print("3. View Expense History")
        print("4. Export Expenses to CSV")
        print("5. Set Budget")
        print("6. Logout")
        print("7. Reset Password")

        choice = input("Enter your choice: ")

        if choice == "1":
            expense = get_expense_details()
            expenses.append(expense)
            print("Expense added successfully!")

        elif choice == "2":
            expenses_by_category(expenses)

        elif choice == "3":
            expense_history(expenses)

        elif choice == "4":
            export_csv(expenses)

        elif choice == "5":
            budget = set_budget()

        elif choice == "6":
            print("Logging out...")
            password = None  # Reset the password when logging out
            registered = False
            main()

        elif choice == "7":
            reset_password()
            main()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()