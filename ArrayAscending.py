arr = [5, 2, 8, 7, 1]
temp = 0
for i in range (len(arr)):
    for j in range (i+1,len(arr)):
        if(arr[i]>arr[j]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
for i in range(len(arr)):
    print(arr[i])
