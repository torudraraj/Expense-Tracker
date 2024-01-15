import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

expense_types = ["Groceries", "Utilities", "Transportation", "Entertainment", "Dining Out", "Other"]

def total_expenses(expenses):
    total = np.sum([expense[2] for expense in expenses])
    return total

def avg_expenses(expenses):
    average = np.mean([expense[2] for expense in expenses])
    return average

def std_dev(expenses):
    std_dev = np.std([expense[2] for expense in expenses])
    return std_dev

def expenses_by_category(expenses):
    categories = set(expense[1] for expense in expenses)
    category_totals = []
    x_labels = []

    print("Expense Analysis by Category:")
    for category in categories:
        category_total = np.sum([expense[2] for expense in expenses if expense[1] == category])
        category_totals.append(category_total)
        x_labels.append(category)
        print(f"{category}: {category_total}")

    total_expenses_value = total_expenses(expenses)
    print(f"\nTotal Expenses: {total_expenses_value}")

    # Bar Chart
    plt.bar(x_labels, category_totals)
    plt.xlabel("Expense Category")
    plt.ylabel("Total Expenses")
    plt.title("Expense Analysis by Category")
    plt.show()

def expense_history(expenses):
    try:
        start_date = datetime.strptime(input("Enter start date (MM-DD-YYYY): "), "%m-%d-%Y")
        end_date = datetime.strptime(input("Enter end date (MM-DD-YYYY): "), "%m-%d-%Y")
    except ValueError:
        print("Invalid date format. Please enter the date in MM-DD-YYYY format.")
        return

    filtered_expenses = []

    for expense in expenses:
        expense_date = datetime.strptime(expense[0], "%m-%d-%Y")
        
        if start_date <= expense_date <= end_date:
            filtered_expenses.append(expense)

    if not filtered_expenses:
        print("No expenses found within the specified date range.")
        return

    print("\nExpense History:")
    for i, expense in enumerate(filtered_expenses, start = 1):
        print(f"{i}. Date: {expense[0]}, Category: {expense[1]}, Amount: {expense[2]}")

    total_expenses_value = total_expenses(expenses)
    average_expenses_value = avg_expenses(expenses)
    std_dev_expenses_value = std_dev(expenses)

    print(f"\nTotal Expenses: {total_expenses_value}")
    print(f"Average Expenses: {average_expenses_value}")
    print(f"Standard Deviation of Expenses: {std_dev_expenses_value}")

def export_csv(expenses):
    df = pd.DataFrame(expenses, columns=["Date", "Category", "Amount"])
    df.to_csv("expenses.csv", index=False)
    print("Expenses exported to 'expenses.csv' successfully.")

def set_budget():
    budget = float(input("Enter your budget: "))
    return budget