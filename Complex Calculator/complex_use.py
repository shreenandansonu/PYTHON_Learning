from complex import *

c1=ComplexNumber(5,-6)
c1.ShowNum()
c2=ComplexNumber(10,9)
c2.ShowNum()
c3=c1+c2
c3.ShowNum()
(c3-c2).ShowNum()
(c1*c2).ShowNum()
print(c1.magnitude())
c1.conjugate().ShowNum()
(c1/c2).ShowNum()
