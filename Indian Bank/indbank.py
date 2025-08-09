import bankdatabase 

class Bankaccount:
    def __init__(self,name:str,fname:str,dob:str,balance:float):
        self.name=name
        self.fname=fname
        self.dob=dob
        self.balance=balance
        print( bankdatabase.create_account(name,fname,dob,balance))
    
    def change_password(self,name:str,password:str,npassword:str):
        return bankdatabase.change_password(name,password, npassword)




bankdatabase.change_password("Shree","Shr0101Kum", "ShreeKumar123")