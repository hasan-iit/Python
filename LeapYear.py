year = int(input("Enter a Year: "))

if ((year%400==0) or (year%100!=0) and (year%4==0)):
    print("Year is LeapYear")
else:
    print("Not Leap Year")