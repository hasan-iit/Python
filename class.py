class Summ:
    def add(self,a,b):
        return a+b
class Substract:
    def sub(self,a,b):
        return a-b
class Mul(Summ,Substract):
    def mul(self,a,b):
        return a*b
m=Mul()
print(m.add(10,20))
print(m.sub(20,10))
print(m.mul(10,10))

# class Employee:
#     count = 0
#     def __init__(self,id,name):
#         Employee.count = Employee.count + 1
#         self.id = id
#         self.name = name
#         print("Count Value:%d" % Employee.count)
#     def display(self):
#         print("Id: %d Name:%s"%(self.id,self.name))
#
# emp = Employee(22,'Shahed')
# emp1 = Employee (20,'Sami')
#
# emp.display()
# emp1.display()
#
# print("Count Value:", Employee.count)
# print(emp.__dict__)
