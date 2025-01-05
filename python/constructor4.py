class Test():
    def __init__(self,x,y=60):
        self.a=x
        self.b=y
        # print("val of a :{}".format(self.a))
        # print("val of b :{}".format(self.b))
t1=Test(30,40)
print("content of t2 :",t1.__dict__)
t2=Test(60,9)
print("content of t3 :",t2.__dict__)
t3=Test(y=939,x=7282)
print("content of t4 :",t3.__dict__)
t4=Test(x=757)
print(t4.__dict__)