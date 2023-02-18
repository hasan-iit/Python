# Method 2: By using comma operator

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

a,b = b,a
print("Swaping: a={0} b={1}".format(a,b))

#By using Arithmetic operation
p = int(input("Enter value p: "))
q = int(input("Enter value Q: "))
p = p+q
q = p-q
p = p-q
print("P={0}, Q={1}".format(p,q))