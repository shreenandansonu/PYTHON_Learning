def factorial (n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
while True:
    inp=int(input("Enter the number of which factorial is needed:"))
    print(factorial(inp))