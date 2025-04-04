# class Car:
#     color="red"
#     brand="Tata"

# nano=Car()
# nano.brand="TATA"
# print(nano.brand)
#______________________________________________________________________________


# class Student:
#     collegeName="CMC Vellore"
#     country="India"
#     def __init__(self,fullname,rollnumber,age,country="India"):
#         self.name=fullname
#         self.rollno=rollnumber
#         self.age=age
#         self.country=country
#     def canVote(self):
#         if(int(self.age)<18):
#             print("Cannot Vote")
#         else:
#             print("Can Vote")

# name,rollnumber,age=input("Please enter name rollnumber and age :").split(" ")
# s1=Student(name,rollnumber,age)
# print(s1.name)
# print(s1.rollno)
# print(s1.collegeName)


#_____________________________________________________________________________

# class Student:
#     @staticmethod
#     def welcomNote():
#         print("This is a welcome note for you.")
#     def __init__(self,name=" ",maths=0,physics=0,chemistry=0):
#         self.name=name
#         self.maths=int(maths)
#         self.physics=int(physics)
#         self.chemistry=int(chemistry)
#     def marksAverage(self):
#         sum=self.maths+self.physics+self.chemistry
#         average=sum/3
#         return average
    
# name,maths,physics,chemistry=input("Enter Name and 3 Marks: ").split(" ")
# s1=Student(name,maths,physics,chemistry)
# s1.welcomNote()#_____________________________________________________________________________

class Account:
    def __init__(self,Name,Password,Amount=0):
        self.Name=Name
        self.__Password=Password
        self.Amount=Amount

    def changePassword(self,newPassword):
        print(self.__Password)
        self.__Password=newPassword
        print(self.__Password)
    

a1=Account("Shreenandan",1234,2000)
a1.changePassword(3456)
print(a1.__Password)