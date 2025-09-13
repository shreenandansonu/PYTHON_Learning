# i=17
# i=i>>1
# print(i)
# i=i<<3
# print(i)

j=1733
s=[]
while j>0:
    k=j&1
    s.append(k)
    j=j>>1
for i in range(len(s)-1,0,-1):
    print(s[i],end="")