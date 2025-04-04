import pandas as pd
class Account:
    SerialNo=0
    def __init__(self,name,initAmt=0,pswd="1234"):
        self.balance=float(initAmt)
        self.name=name
        self.__pswd=pswd
        with open("Banking System/accounts.csv","a+") as adb:
            adb.write(f"\n{self.name},{self.balance},{self.__pswd}")
            adb.close()
        print("_________________________________\n")
        print(f"✅ Account  {self.name} Created.✨\n💵 Initial Amount is Rs {self.balance:.2f}.\n")
        print("_________________________________\n")

    @staticmethod
    def GetBalance(name,pswdin):
        df=pd.read_csv("Banking System/accounts.csv")
        x=0
        while True:
            if name == df["Name"][x]:
                if pswdin ==str(df["Password"][x]):
                    balance = df["Amount"][x]
                    print(f"Your Current Balance is {balance}")
                    break
                else:
                    print("⚠️ Wrong Password ⚠️")
                    break
            else:
                x+=1
            
        print("_________________________________\n")

