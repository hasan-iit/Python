list1=[]
n = int(input("Enter number of items: "))
for i in range(n):
    list1.append(int(input("Enter list item: ")))
print(list1)
item = int(input("Enter searching item: "))
low=0
high=len(list1)-1
mid = 0

while(low<=high):
    mid = int(int(low+high)/2)
    if(list1[mid]<item):
        low=mid+1
    elif(list1[mid]>item):
        high=mid-1
        # mid = low/high//2
    elif (item==list1[mid]):
        print("Item found and position is:",mid+1)
        break
    else:
        print("Item not found")