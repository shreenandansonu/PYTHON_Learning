class bankaccount:

    def __init__(self, acc_name ,initialAmt): 
        self.acc_name = acc_name
        self.bal = initialAmt
        
        print("\nAccount :" ,self.acc_name )
        print("\nBalance = " ,self.bal )



    def GetBalance(self):
         print(f"\nBalance in {self.acc_name} account is {self.bal}\n")


    def deposit(self, amt): 
          self.bal = self.bal + (amt * 1.05) # Giving 5% interest
          print(f"\nDeposite complete into {self.acc_name} account\n")
          self.GetBalance()  
    

class savingsAcct(bankaccount):
    def __init__(self, acc_name, initialAmt):
        super().__init__(acc_name, initialAmt)
        self.fee = 5 # Addiing 5/- penalty for withdrawal 

    def withdrawal(self, amt):
        if self.bal >= amt + self.fee:
            self.bal -= (amt + self.fee)
            print("Withdraw complete with fee\n")
            print(f"\nRemaining balance in {self.acc_name} is {self.bal}")
            return True
        else:
            print("Insufficient balance (including fee)")
            return False
        
    def Transfer(self,acc2, amt):
        if self.withdrawal(amt): # if the withdrawal passes then only deposit orelse not deposited in second account 
            acc2.deposit(amt)
            print(f"\nAmount transfered {amt}, Total balance left in {self.acc_name} is {self.bal}")
        else:
            print(f"\nInsufficient balance\n")