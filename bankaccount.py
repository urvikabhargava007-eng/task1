class BankAccount:
    def __init__(self, name, mobile, age, dob, balance):
        self.name = name
        self.mobile = mobile
        self.age = age
        self.dob = dob
        self.balance = balance

    def show_info(self):
        print("\n--- Account Details ---")
        print(f"Name:           {self.name}")
        print(f"Mobile:         {self.mobile}")
        print(f"Age:            {self.age}")
        print(f"DOB:            {self.dob}")
        print(f"Current Balance: ₹{self.balance:}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited ₹{amount:}.")
            print(f"New Balance: ₹{self.balance:}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print(f"Insufficient funds. Current balance: ₹{self.balance:}")
        else:
            self.balance -= amount
            print(f"Successfully withdrew ₹{amount:}.")
            print(f"New Balance: ₹{self.balance:}")


def find_account(accounts, mobile):
    for acc in accounts:
        if acc.mobile == mobile:
            return acc
    return None



all_accounts = []

while True:
    print("\n" + "-" * 30)
    print(" BANK MANAGEMENT SYSTEM ")
    print("-" * 30)
    print("A. Create New Account")
    print("B. Check Account Details")
    print("C. Deposit Money")
    print("D. Withdraw Money")
    print("E. Exit")
    print("-" * 30)

    user_data = input("Enter your choice (A-E): ").strip().upper()

   
    match user_data:
        case "A":
            mobile = input("Enter mobile number: ").strip()
            
            if find_account(all_accounts, mobile):
                print("Warning: An account with this mobile number already exists.")
            else:
                name = input("Enter full name: ").strip()
                age = input("Enter age: ").strip()
                dob = input("Enter date of birth (DD/MM/YYYY): ").strip()
                try:
                    balance = float(input("Enter initial deposit amount: ").strip())
                    new_acc = BankAccount(name, mobile, age, dob, balance)
                    all_accounts.append(new_acc)
                    print(f"Account successfully created for {name}!")
                except ValueError:
                    print("Error: Balance must be a valid number.")

        case "B":
            mobile = input("Enter mobile number: ").strip()
            account = find_account(all_accounts, mobile)
            if account:
                account.show_info()
            else:
                print("Account not found.")

        case "C":
            mobile = input("Enter mobile number: ").strip()
            account = find_account(all_accounts, mobile)
            if account:
                try:
                    amount = float(input("Enter amount to deposit: ").strip())
                    account.deposit(amount)
                except ValueError:
                    print("Error: Amount must be a valid number.")
            else:
                print("Account not found.")

        case "D":
            mobile = input("Enter mobile number: ").strip()
            account = find_account(all_accounts, mobile)
            if account:
                try:
                    amount = float(input("Enter amount to withdraw: ").strip())
                    account.withdraw(amount)
                except ValueError:
                    print("Error: Amount must be a valid number.")
            else:
                print("Account not found.")

        case "E":
            print("Thank you for using the Banking System. Goodbye!")
            exit(0)

        case _:
            print("Invalid selection! Please enter A, B, C, D, or E.")