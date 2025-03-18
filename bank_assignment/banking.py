# Banking System & Transaction History

# (1) Initialize user balance and transaction history
balance = 0.0
transaction_history = []

# (2) Function to deposit money
def deposit(amount):
    global balance
    if amount > 0:
        balance += amount
        transaction_history.append(f"Deposit: ₹{amount:.2f} | Balance: ₹{balance:.2f}")
        print(f"✅ ₹{amount:.2f} successfully deposited. Current balance: ₹{balance:.2f}")
    else:
        print("❌ Invalid amount! Please enter a positive value.")

# (3) Function to withdraw money
def withdraw(amount):
    global balance
    if amount > 0 and amount <= balance:
        balance -= amount
        transaction_history.append(f"Withdrawal: ₹{amount:.2f} | Balance: ₹{balance:.2f}")
        print(f"✅ ₹{amount:.2f} successfully withdrawn. Remaining balance: ₹{balance:.2f}")
    elif amount > balance:
        print("❌ Insufficient balance!")
    else:
        print("❌ Invalid amount! Please enter a positive value.")

# (4) Function to check current balance
def check_balance():
    print(f"💰 Your current balance is: ₹{balance:.2f}")

# (5) Function to display transaction history
def show_transaction_history():
    if transaction_history:
        print("\n📜 Transaction History:")
        for transaction in transaction_history:
            print(transaction)
    else:
        print("\n📜 No transactions found.")

# (6) Main menu loop
while True:
    print("\n🔹 Banking System Menu 🔹")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. View Transaction History")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # Validate input choice
    if choice not in ["1", "2", "3", "4", "5"]:
        print("❌ Invalid choice! Please enter a number between 1 and 5.")
        continue

    # Handle user choices
    if choice == "1":
        amount = input("Enter the amount to deposit: ₹")
        if not amount.replace(".", "", 1).isdigit() or float(amount) <= 0:
            print("❌ Invalid amount! Please enter a valid positive number.")
        else:
            deposit(float(amount))

    elif choice == "2":
        amount = input("Enter withdrawal amount: ₹")
        if not amount.replace(".", "", 1).isdigit() or float(amount) <= 0:
            print("❌ Invalid amount! Please enter a positive number.")
        elif float(amount) > balance:
            print(f"❌ Insufficient balance! Your current balance is ₹{balance:.2f}")
        else:
            withdraw(float(amount))

    elif choice == "3":
        check_balance()

    elif choice == "4":
        show_transaction_history()

    elif choice == "5":
        print("✅ Thank you for using the Banking System. Have a great day! 😊")
        break  # Exit the loop

print("Exiting Banking System. Goodbye!")

from datetime import datetime

class Transaction:
    def __init__(self, amount, timestamp=None):
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number.")
        self.amount = float(amount)
        self.timestamp = timestamp if timestamp else datetime.now()

    def __repr__(self):
        return f"Transaction({self.amount}, {repr(self.timestamp)})"

    def __str__(self):
        sign = "+" if self.amount >= 0 else "-"
        return f"{self.timestamp.strftime('%Y-%m-%d')}: {sign}${abs(self.amount):,.2f}"

class Account:
    def __init__(self):
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.transactions.append(Transaction(amount))

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        self.transactions.append(Transaction(-amount))

    def get_balance(self):
        return sum(transaction.amount for transaction in self.transactions)
