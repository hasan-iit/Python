def sum(num1,num2):
    return num1+num2
def substract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2
print("Enter your choice- a for Add,b for substracr,c for multiply,d for dividation:")
choice = input("Enter a/b/c/d: ")
# print("Enter two number: ")
num1 = int(input("Enter First number: "))
num2 = int(input("Enter your secoond number: "))
if choice=='a':
    print(sum(num1,num2))
elif choice=='b':
    print(substract(num1,num2))
elif choice=='c':
    print(multiply(num1,num2))
elif choice=='d':
    print(divide(num1,num2))
else:
    print("Invalid choice")
