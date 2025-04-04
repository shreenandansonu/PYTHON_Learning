# name=input("Enter your Name: ")
# print(len(name))

# statement=input("Enter Sentance: ")
# print(statement.count("&"))

# age=int(input("Enter Your age: "))
# if(age<18):
#     print("Cannot Vote")

# str="la la la lala na ana"
# # print(not(str.endswith("in")))
# print(str.count("na"))

# names=list(input("Enter 3 Names of movies: ").split(" "))
# if(names.copy()==names.reverse()):
#     print("Palindrome")


# dict={}
# dict["Name"]="Shreenandan Sahu"
# dict["Age"]=23
# dict["Interest"]={"Engineering":100,"Startup":100,"Success":100}
# print(dict["Interest"]["Engineering"])

# collection=set( )
# collection.add("Suraksha")
# collection.add("Shreenandan")
# print(collection)
# print(len(collection))

# meaning={"table":["a piece of furniture","list of facts and figures"],"cat":"a small animal"}
# print(meaning["table"])

# subjects=["py","Java","C++","py","js","Java","py","Java","C++","C"]
# print(len(set(subjects)))

# marks={"maths":None,"Physics":None,"Chemistry":None}
# marks["maths"]=input("Marks: ")
# marks["Physics"]=input("Marks: ")
# marks["Chemistry"]=input("Marks: ")
# print(marks)


# value={9,"9.0",9.01}
# print(value)

# def my_sum(a=2,b):
#     return(a+b)

# print(my_sum(5))



#write a recursive function to calculate the sum of first n natural numbers




# def sum(n):
#     if n==0:
#         return 0
#     suma=sum(n-1)+n
#     return suma

# num=int(input("Enter Number: "))
# print(sum(num))



# def print_list(list,index=0,end=None):
#     if(index==len(list) or index==end+1):
#         return
#     print(list[index])
#     print_list(list,index+1,end)

# fruits=["apple","banana","guava","pomogranate","chicku","watermellon","jackfruit"]

# print_list(fruits,3,5)

# with open("sonu.txt","r") as f:
#     data=f.read()
#     print(data)
#     nums=list(data.split(","))
#     count=0
#     for x in nums:
#         if(int(x)%2==0):
#             print(x,end=" ")
#             count+=count
#     else:

#         print(f"\nTotal number of even numbers is: {count}")