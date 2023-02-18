arr = []
print("Enter 10 array elements:")
for i in range(10):
    user_input = input()
    if user_input:
        arr.append(str(int(user_input)))
print(arr)
print("Reverse array is: ",end="")
for j in range(len(arr)-1,-1,-1):
    print(arr[j],"\t",end="")