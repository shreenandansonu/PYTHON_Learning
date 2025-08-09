class Students:
    def __init__(self,name:str,age:int,marks:int):
        self.name= name
        self.age=age
        self.marks=marks
        
    def GetMarks(self):
        return self.marks
    
class Subject:
    def __init__(self,name,max_stud):
        self.name=name
        self.max_stud = max_stud
        self.students=[]

    def AddStudent(self, student):
        if len(self.students)<self.max_stud:
            self.students.append(student)
            return True
        else:
            return False
    def GetAvgMarks(self):
        if not self.students: return 0
        else:
            total_marks=0
            for student in self.students:
                print(f"{student.name} has {student.GetMarks()} out of 100")
                total_marks+=student.GetMarks()
                
            return total_marks/len(self.students)
        
s1=Students("Shreenandan",23,99)
s2=Students("Rohit",22,95)
s3=Students("Amit",24,90) 
s4=Students("Ravi",21,85) 

sub1=Subject("Maths",2)
print(sub1.AddStudent(s1))
print(sub1.AddStudent(s2))
print(sub1.AddStudent(s3))
print(sub1.AddStudent(s4)) 
print((sub1.GetAvgMarks()))


