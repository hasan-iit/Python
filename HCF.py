num1 = int(input("Enter num1: "))
num2 = int(input("Enter Num2: "))
if(num1>num2):
    big = num1
else:
    big = num2
for x in range(2,big+1):
    if((num1%x==0)and(num2%x==0)):
        hcf = x
print(hcf)