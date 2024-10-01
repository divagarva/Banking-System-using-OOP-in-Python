# Bank Account class
class BankAccount:
    def __init__(self, account_holder_name, account_number, balance=0.0):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = balance

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance:.2f}")
        else:
            print("Insufficient balance or invalid amount.")

    # Method to display account details
    def display_account_details(self):
        print("\n=== Account Details ===")
        print(f"Account Holder: {self.account_holder_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.balance:.2f}")
        print("========================\n")


# Main program
def main():
    # Creating a new bank account
    account_holder = input("Enter account holder's name: ")
    account_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance: "))

    account = BankAccount(account_holder, account_number, initial_balance)

    # Displaying account details
    account.display_account_details()

    while True:
        print("Choose an option:")
        print("1. Deposit money")
        print("2. Withdraw money")
        print("3. Show account details")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            deposit_amount = float(input("Enter amount to deposit: "))
            account.deposit(deposit_amount)
        elif choice == '2':
            withdraw_amount = float(input("Enter amount to withdraw: "))
            account.withdraw(withdraw_amount)
        elif choice == '3':
            account.display_account_details()
        elif choice == '4':
            print("Thank you for using our banking system.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
