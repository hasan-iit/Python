list = []
print("Enter Number of List Element: ")
n = int(input())
for i in range(n):
    list.append(input())
print(list)
list.append('Father')
print(list)
list.insert(3,6)
print(list)
list.extend(["Rasel","Nigar"])
print(list)
list.extend("Apple")
print(list)