number = int (input("Enter a Number: "))
n1 = 0
n2 = 1
print("{0}\t{1}".format(n1,n2),end="")
for x in range(2,number):
    n3 =n1+n2
    print("\t{0}".format(n3),end="")
    n1 =n2
    n2=n3
