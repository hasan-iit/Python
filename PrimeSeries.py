lower_level = int(input("Enter Lower number in Range: "))
upper_level = int(input("Enter Upper Number in Range: "))
count = 0
for number in range(lower_level,upper_level+1):
    count=0
    for x in range(2,int(number/2)+1):
        if(number%x)==0:
            count = count+1
            break
    if(count==0):
        print(number)


# factorial of given number
# def fact(n):
#     return 1 if (n == 1 or n == 0) else n * fact(n - 1);
#
#
# num = 5
# print("Factorial of", num, "is", )
# fact(num)