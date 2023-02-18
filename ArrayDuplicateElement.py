arr = []
print("Enter 10 array element: ")
for i in range(11):
    arr.append(int(input()))
print(arr)
print("Duplicate El1ement: ")
for j in range(len(arr)):
    for k in range(j+1,len(arr)):
        if (arr[j]==arr[k]):
            print(arr[k],"\t",end="")

