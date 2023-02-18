def fibonacci(num):
    if int(num)<=0:
        return 0
    elif int(num)==1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)

num = int(input("Enter a Number: "))
for x in range(num):
    print(fibonacci(x))
