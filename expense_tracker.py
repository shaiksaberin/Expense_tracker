# Simple Expense Tracker

expenses = []

def add_expense():
    try:
        amount = float(input("Enter amount: ₹"))
        category = input("Enter category (e.g., Food, Travel): ")
        expenses.append({'amount': amount, 'category': category})
        print("✅ Expense added!\n")
    except ValueError:
        print("❌ Invalid input. Try again.\n")

def show_expenses():
    if not expenses:
        print("No expenses recorded yet.\n")
        return

    total = 0
    print("\n--- Expense List ---")
    for e in expenses:
        print(f"{e['category']}: ₹{e['amount']}")
        total += e['amount']
    print(f"Total Spent: ₹{total}\n")

def main():
    while True:
        print("=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. Show Expenses")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            show_expenses()
        elif choice == '3':
            print("Goodbye! 👋")
            break
        else:
            print("Invalid option. Try again.\n")

main()
