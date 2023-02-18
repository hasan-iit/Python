List = []
n = int(input("Enter number of list item: "))
for i in range(n):
    List.append(int(input("Enter list item: ")))
print(List)
search_index = -1
search_item = int(input("Enter Search item: "))
for i in range(len(List)):
    if(List[i]==search_item):
        search_index =i
        break
if (search_index!=-1):
    print("item found and position is: ",search_index)
else:
    print("item not found")