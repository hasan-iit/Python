dic = {}
dic = dict({1:'Python',2:'Machine Learning'})
print(dic)

employee = {}
n = int(input("How many employee you want to add: "))
for i in range(n):
    name = input("Enter Employee Name: ")
    salary = input("Enter Employee Salary: ")
    employee[name]=salary
print(employee)
employee['Sawad']=30000
print(employee)
dic.update(employee)
print(dic)
dic.clear()
print(dic)
print(sorted(employee.items()))