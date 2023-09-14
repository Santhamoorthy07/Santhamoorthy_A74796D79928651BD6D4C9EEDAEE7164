class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        return f"Account Holder: {self.__account_holder_name}\nAccount Number: {self.__account_number}\nAccount Balance: ${self.__account_balance:.2f}"
# Creating an instance of the BankAccount class
my_account = BankAccount("12345", "John Doe", 1000.00)

# Testing deposit and withdraw functionality
print(my_account.display_balance())  # Display initial balance

if my_account.deposit(500.50):
    print("Deposited $500.50")
else:
    print("Invalid deposit amount")

if my_account.withdraw(200.75):
    print("Withdrawn $200.75")
else:
    print("Invalid withdrawal amount")

print(my_account.display_balance())  # Display updated balance
