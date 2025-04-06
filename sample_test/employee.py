class Employee:
    def __init__(self,name:str,age:int,gender:chr,mno:str)->None:
        """This Creates an instance of the Employee class"""
        self.name=name
        self.age=age
        self.gender=gender
        self.mobileNumber=mno
        self.email:str=f"{self.name}@gmail.com"
    def __str__(self)-> str:
        """This function returns the details of the employee added"""
        return f"Name:- {self.name}\nAge:- {self.age}\nGender:- {self.gender}\nMobile Number:- {self.mobileNumber}\nEmail Address:- {self.email}"

e1=Employee("Shreenandan",24,'M',7848938270)
print(e1)
