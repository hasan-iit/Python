import collections
list1 = [11, 12, 13, 14, 15]
list2 = [12, 13, 11, 15, 14]

a= set(list1)
b=set(list2)
if a==b:
    print("List are same")
else:
    print("List are not same")
list1.sort()
print(list1)

list3 = [10, 20, 30, 40, 50, 60]
list4 = [10, 20, 30, 50, 40, 70]
list5 = [50, 10, 30, 20, 60, 40]

if(collections.Counter(list3)==collections.Counter(list5)):
    print("List3 and List5 are same")
else:
    print("List3 and List5 are not same")