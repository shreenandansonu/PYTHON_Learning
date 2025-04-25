# cook your dish here
testcase = int(input())

for i in range(testcase):
    count = 0
    N = int(input())
    A = list(map(int,input().split()))
    for a in A:
        if a > 1:
            count+=(a-1)
    print(count)