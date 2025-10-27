def factorial (n):
    if n==0:
        return 1 #stops here and does not call negative numbers
    else:
        return n*factorial(n-1)
while True:
    inp=int(input("Enter the number of which factorial is needed:"))
    print(factorial(inp))

    