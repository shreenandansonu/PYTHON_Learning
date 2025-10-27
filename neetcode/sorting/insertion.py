def insertionsort(arr):
    #iterating through each element 
    for i in range(1,len(arr)):#first pointer
        j=i-1 #second Pointer
        while (j>=0 and arr[j]>arr[j+1]):#comparg both the pointers
            #swapping the elements
            temp=arr[j+1]
            arr[j+1]=arr[j]
            arr[j]=temp
            j-=1
    return arr

arr=list(map(int,input("Enter the elements of array:").split(", ")))
print(insertionsort(arr))

