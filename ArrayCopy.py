arr1 = [1,2,3,4,5];
arr2 = [None] * len(arr1);

for x in range(0,len(arr1)):
    arr2[x] = arr1[x]
    # print(arr2)
print("Elements of new array: ");
for i in range(0, len(arr2)):
   print("\t",arr2[i],end='')