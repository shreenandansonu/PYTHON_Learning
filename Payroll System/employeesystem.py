from payrollsystem import *

with open("Payroll System\class.csv","r") as data:
    try:
        while True:
            name,basePay,Salary,TA,MA=data.readline().split(",")
            name=PermantntEmployeeClass(name,basePay,Salary,TA,MA)
            name.showClass()
            print("_________XXXXXX________")
    except Exception as e:
        print(f"No More Class and {e}" )