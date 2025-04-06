#This module deals with Complex Calculation
# This uses the OOPS concepts of Abstraction,Encapsulation and Polymorphisim. 

import math
class ComplexNumber():
    def __init__(self,a=0,b=0):
        self.real=a
        self.imaginary=b

    def ShowNum(self):
        if self.imaginary<0:
            print(f"{self.real:.3f} - {abs(self.imaginary):.3f} j")
        else:
            print(f"{self.real:.3f} + {abs(self.imaginary):.3f} j")
        
    # Addition of Complex numbers
    def __add__(self,a):
        b=self.real + a.real
        c=self.imaginary + a.imaginary
        return ComplexNumber(b,c)

    # Subtraction of Complex numbers
    def __sub__(self,a):
        b=self.real - a.real
        c=self.imaginary - a.imaginary
        return ComplexNumber(b,c)
    
    # Multiplication of Complex numbers
    def __mul__(self,a):
        b=self.real*a.real - self.imaginary*a.imaginary
        c=self.real*a.imaginary + self.imaginary*a.real
        return ComplexNumber(b,c)
    
    # Division of Complex numbers
    def __truediv__(self,b):
        c=self.__mul__(b.conjugate())
        a=int(c.real)/(float(b.magnitude())**2)
        d=int(c.imaginary)/(float(b.magnitude())**2)
        return ComplexNumber(a,d)
    
    #Conjugate of Complex Number
    def conjugate(self):
        b=(-1)*self.imaginary
        return ComplexNumber(self.real,b)
    
    #Magnitude of Complex Number
    def magnitude(self):
        a=self.real**2
        b=self.imaginary**2
        return (f"{math.sqrt(a+b):.3f}")
