class PermantntEmployeeClass():
    def __init__(self,name,basePay,Salary,TA,MA):
        self.className=name #class name
        self.basePay=basePay #base pay amount
        self.Salary=Salary #salary amount
        self.TA=TA #Travell Allowance 
        self.MA=MA #Medical Allowance
        self.TotalPayable=(int(self.basePay)+int(self.Salary)+int(self.TA)+int(self.MA))
    def showClass(self):
        print(f"Class Name = {self.className}")
        print(f"Base Salary = {self.basePay}")
        print(f"Salary = {self.Salary}")
        print(f"Travel Allowance = {self.TA}")
        print(f"Medical Allowance = {self.MA}")
        print(f"Total Payable Salary ={self.TotalPayable}")
        
# class ContractEmployeeClass():
#     def __init__(self,name,Workhour,Rate):
#         self.name=name
#         self.WH=Workhour
#         self.RT=Rate
    
#     def paybale(self):
#         return int(self.WH)*int(self.RT)

# class CreateEmploye():
#     def __init__(self,Name,Position,Employee_ID):
#         self.Ename=Name
#         self.Position=Position
#         self.EID=Employee_ID
   
#     def details(self):
#         return  self.Ename,self.Position,self.EID


