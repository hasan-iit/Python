number = int(input("Enter a Number: "))
temp = number
sum = 0

while(number!=0):
    s = number%10
    sum = sum+(s*s*s)
    number = int(number/10)
print(sum)
if(sum==temp):
    print("Number is Amstrong")
else:
    print("Not Amstrong")