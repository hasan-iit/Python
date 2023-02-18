number = int(input("Enter a Number: "))
print("Multiplication Table of a {0} is:".format(number))
for x in range(1,11):
    print(number,'x',x, '=',number*x)