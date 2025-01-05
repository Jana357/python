class Employee():
    def __init__(self,empno,ename):
        self.enum=empno
        self.employee=ename
e1=Employee(10,"jana")
print("content of e1 :",e1.__dict__)
e2=Employee(20,"Raju")
print("content of e2 :",e2.__dict__)