from datetime import date
import json 
import os

expenses = []
expense_id = 1


def show_menu():
    print("\n SMART EXPENSE TRACKER ")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Exit")


def add_expense():
    global expense_id

    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be greater than 0")
            return
    except ValueError:
        print("Invalid amount")
        return

    category = input("Enter category: ").strip().title()
    if not category:
        print(" Category cannot be empty")
        return

    description = input("Enter description: ").strip()
    if len(description) < 3:
        print("Description must be at least 3 characters")
        return

    today = date.today().isoformat()

    expense = {
        "id": expense_id,
        "amount": amount,
        "category": category,
        "description": description,
        "date": today
    }

    expenses.append(expense)
    expense_id += 1
    save_expenses()

    print("Expense added successfully")


def view_expenses():
    if not expenses:
        print("No expenses found")
        return

    print("\nEXPENSE LIST")
    for exp in expenses:
        print(
            f"ID: {exp['id']} | ₹{exp['amount']} | "
            f"{exp['category']} | {exp['description']} | {exp['date']}"
        )
    print("=" * 30)


def delete_expense():
    if not expenses:
        print("No expenses to delete")
        return

    try:
        delete_id = int(input("Enter expense ID to delete: "))
    except ValueError:
        print("Invalid ID")
        return

    for exp in expenses:
        if exp["id"] == delete_id:
            expenses.remove(exp)
            save_expenses()
            print("Expense deleted successfully")
            return

    print("Expense ID not found")


def load_expenses():
    global expenses, expense_id

    if not os.path.exists("expenses.json") or os.path.getsize("expenses.json") == 0:
        expenses = []
        return

    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
            if expenses:
                expense_id = expenses[-1]["id"] + 1
    except json.JSONDecodeError:
        expenses = []

load_expenses()


def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)


while True:
    show_menu()
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        delete_expense()
    elif choice == "4":
        print("Exiting program")
        break
    else:
        print("Invalid choice")
