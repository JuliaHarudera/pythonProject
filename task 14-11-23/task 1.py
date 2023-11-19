class Account:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited {amount}. New balance: {self._balance}")

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient funds.")
        else:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance: {self._balance}")

    def __setattr__(self, name, value):
        if name == "_balance":
            raise AttributeError("Cannot directly set the balance. Use the deposit and withdraw methods instead.")
        super().__setattr__(name, value)

    def __getattr__(self, name):
        raise AttributeError(f"'Account' object has no attribute '{name}'")


account = Account(initial_balance=1000)


try:
    account.balance = 1500
except AttributeError as e:
    print(f"Error: {e}")


account.deposit(500)
account.withdraw(200)


try:
    print(account.nonexistent_property)
except AttributeError as e:
    print(f"Error: {e}")
