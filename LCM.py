number1 = int(input("Enter First Number: "))
number2 = int(input("Enter Number2: "))
if(number1>number2):
    max_div = number1
else:
    max_div = number2

while(True):
    if((int(max_div%number1)==0) and int((max_div%number2)==0)):
        #lcm = max_div
        print(max_div)
        break
    else:
        max_div+=1