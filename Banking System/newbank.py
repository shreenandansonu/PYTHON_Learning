class BankAcc():
    def __init__(self,name:str,amount:int):
        self.amount=amount
        self.name=name

    def ShowBalance(self):
        print(f"Account:- {self.name}\n Amount:- {self.amount}")

    def Deposite(self,amount)->int:
        self.amount+=amount
    
    def valTrnx(self,amount)->bool:
        if(amount<=self.amount):
            return True
        else:
            return False
    
    def Withdraw(self,amount):
        if self.valTrnx(amount):
            self.amount-=amount
            self.ShowBalance()
        else:
            print(f"{self.name} has no sufficient fund")

    def Transfer(self,other,amount):
        oth:BankAcc=other 
        if self.valTrnx(amount):
            self.amount-=amount
            oth.amount+=amount
            self.ShowBalance()
        else:
            print(f"{self.name} has no sufficient fund")

class SaveAcc(BankAcc):
    withdraw_fee = 5
    transfer_fee = 10
    def Withdraw(self, amount):
        if super().valTrnx(amount+self.withdraw_fee):
            self.amount-=amount+self.withdraw_fee
            self.ShowBalance()
        else:
            print(f"{self.name} has no sufficient fund")
    def Transfer(self, other:BankAcc, amount):
        if super().valTrnx(amount+self.transfer_fee):
            self.amount-=amount+self.transfer_fee
            other.Deposite(amount)
            self.ShowBalance()
        else:
            print(f"{self.name} has no sufficient fund")

class CreditAcc(SaveAcc):# Inheritance
    deposite_reward:float=1.05
    def Deposite(self, amount):
        return super().Deposite(amount*CreditAcc.deposite_reward)