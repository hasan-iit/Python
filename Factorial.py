number = int(input("Enter a number: "))
factorial = 1
if (number<=1):
    factorial = 1
else:
    for x in range(1,number+1):
        factorial = factorial*x
print("Factorial of this number is: ",factorial)


# def factorial(number):
#     if(number<=1):
#         return 1
#     else:
#         return number*factorial(number-1)
#
# number = int(input("Enter a Number: "))
# print("Factorial of this number is: ",factorial(number))