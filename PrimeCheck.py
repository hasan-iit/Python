number = int(input("Enter a number: "))
count = 0
for x in range(2,int(number/2)+2):
    if(number%x)==0:
        count=count+1
        # print("Number is not Prime")
        break
    # else:
    #     print("Prime")
if(count==0):
    print("Number is prime")
else:
    print("Number not Prime")