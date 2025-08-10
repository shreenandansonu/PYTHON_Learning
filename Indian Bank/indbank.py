from bankdatabase import *  # if needed
import random as rd


class Bankaccount:
    def __init__(self, rowid, name, fname, dob, balance, password):
        self.rowid = rowid
        self.name = name
        self.fname = fname
        self.dob = dob
        self.balance = balance
        self.password = password

    @staticmethod
    def generate_password(dob: str) -> str:

        return f"{rd.randint(100,999)}{rd.choice(['@','#','%','*'])}{dob[-2:]}"

    @classmethod
    def create_account(cls, name: str, fname: str, dob: str, balance: float):
        password = cls.generate_password(dob)
        create_account(name, fname, dob, balance, password)
        data = login(name, password)
        print("✅ Account created successfully. Your password is:", password)
        return cls(*data[0]) #this initiates a class object

    @classmethod
    def login(cls, name: str, password: str):
        data = login(name, password)
        if data:
            print("✅ Login successful!")
            return cls(*data[0])
        else:
            print("❌ Invalid credentials.")
            return None
        
    @classmethod
    def delete_account(cls, name:str,password:str,fname:str):
        data = login(name, password)
        if data:
            if name == data[0][1] and fname == data[0][2]:
                print("✅ Account found. Deleting...")
                rowid = data[0][0]
                remove_account(rowid)
                print("✅ Account deleted successfully.")
        else:
            print("❌ Invalid credentials.")
    
    
    def check_balance(self):
        print(f"💰 Your current balance is: {self.balance}")

    def change_password(self, new_password: str):
        change_password(self.rowid, new_password)
        self.password = new_password
        print("✅ Password changed successfully")

    def withdraw(self, amount: float):
        if amount*(1.001) <= self.balance:
            self.balance -= amount*(1.001)
            updating_database(self.rowid, 'balance', self.balance)
            print(f"✅ Withdrawal successful. New balance: {self.balance}")
        else:
            print("❌ Insufficient balance for withdrawal.")

    def deposite(self, amount: float):
            self.balance += amount*(1-0.001)
            updating_database(self.rowid, 'balance', self.balance)
            print(f"✅ Deposite successful. New balance: {self.balance}")
    

    def transfer(self, amount: float, accountid: int):
        if amount*(1.001) <= self.balance:
            self.balance -= amount*(1.001)
            deposite(accountid, amount*(1))
            updating_database(self.rowid, 'balance', self.balance)
            print(f"✅ Transfer successful. New balance: {self.balance}")
            # Here you would implement the logic to update the receiver's account
            # For now, we just print a message
            print(f"💸 Transferred {amount} to {accountid}.")
        else:
            print("❌ Insufficient balance for transfer.")


# ---------------- Main Program ----------------
while True:
    print("\n=== Welcome to Indian Bank ===")
    print("1. Create Account")
    print("2. Login")
    print("3. Delete Account")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter your name: ")
        fname = input("Enter your father's name: ")
        dob = input("Enter your date of birth (DD/MM/YYYY): ")
        balance = float(input("Enter initial balance: "))
        account=Bankaccount.create_account(name, fname, dob, balance)
        if account:
            while True:
                    print("\n--- Account Menu ---")
                    print("1. Check Balance")
                    print("2. Change Password")
                    print("3. Withdraw Money")
                    print("4. Deposite Money")
                    print("5. Transfer Money")
                    print("6. Logout")
                    sub_choice = input("Enter your choice: ")

                    if sub_choice == '1':
                        account.check_balance()

                    elif sub_choice == '2':
                        new_pass = input("Enter your new password: ")
                        account.change_password(new_pass)
                    elif sub_choice == '3':
                        amount = float(input("Enter amount to withdraw: "))
                        account.withdraw(amount)

                    elif sub_choice == '4':
                        amount = float(input("Enter amount to deposite: "))
                        account.deposite(amount)    
                    elif sub_choice == '5':
                        amount = float(input("Enter amount to transfer: "))
                        accountid = int(input("Enter the account ID to transfer to: "))
                        account.transfer(amount, accountid)

                    elif sub_choice == '6':
                        print("🔓 Logged out.")
                        break


                    else:
                        print("❌ Invalid choice.")


    elif choice == '2':
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        account = Bankaccount.login(name, password)

        if account:  # Start account session
            while True:
                print("\n--- Account Menu ---")
                print("1. Check Balance")
                print("2. Change Password")
                print("3. Withdraw Money")
                print("4. Deposite Money")
                print("5. Transfer Money")
                print("6. Logout")
                sub_choice = input("Enter your choice: ")

                if sub_choice == '1':
                    account.check_balance()

                elif sub_choice == '2':
                    new_pass = input("Enter your new password: ")
                    account.change_password(new_pass)
                elif sub_choice == '3':
                    amount = float(input("Enter amount to withdraw: "))
                    account.withdraw(amount)

                elif sub_choice == '4':
                    amount = float(input("Enter amount to deposite: "))
                    account.deposite(amount)    
                elif sub_choice == '5':
                    amount = float(input("Enter amount to transfer: "))
                    accountid = int(input("Enter the account ID to transfer to: "))
                    account.transfer(amount, accountid)

                elif sub_choice == '6':
                    print("🔓 Logged out.")
                    break


                else:
                    print("❌ Invalid choice.")

    elif choice == '3':
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        fname = input("Enter your father's name: ")
        Bankaccount.delete_account(name, password, fname)  

    elif choice == '4':
        print("Thank you for banking with us!")
        break

    else:
        print("❌ Invalid choice.")

