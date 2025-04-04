from complex import ComplexNumber
with open("Python Begineer\data.txt","r") as data: #please change the directory accordingly
    try:
        while True:
            C1=data.readline()
            a,b=C1.split(",")
            c1=ComplexNumber(int(a),int(b))
            C2=data.readline()
            c,d=C2.split(",")
            
            c2=ComplexNumber(int(c),int(d))
            print(f"Magnitude of the number 1 is: {c1.magnitude()}")
            print(f"Magnitude of the number 12 is: {c2.magnitude()}")
            print(f"Sum of the numbers is: ",end=" ")
            (c1+c2).ShowNum()
            print(f"Difference of the numbers is: ",end=" ")
            (c1-c2).ShowNum()
            print(f"Product of the numbers is: ",end=" ")
            (c1*c2).ShowNum()
            print(f"Ratio of the numbers is: ",end=" ")
            (c1/c2).ShowNum()
            print("___________🐼🐨🐻‍❄️🐻🐸🦓🐽🐒___________\n")
    except Exception as e:
        print("The file data got over. Thank You 😍")
        



