arr = [1,2,3,4,5]
rotation_no=3
for x in range(len(arr)):
    print(arr[x])
for i in range(0,rotation_no):
    first = arr[0]
    for j in range (0,len(arr)-1):
        arr[j]=arr[j+1]
    arr[len(arr)-1] = first
print("After raotation result is: ")
for k in range(len(arr)):
    print(arr[k],"\t",end="")
