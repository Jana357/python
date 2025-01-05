class Test():
    def __init__(self,x=10,y=20):
        self.a=x
        self.b=y
        # print("val of a :{}".format(self.a))
        # print("val of b :{}".format(self.b))
t1=Test( )
print("content of t1 :",t1.__dict__)
t2=Test(30,40)
print("content of t2 :",t2.__dict__)
t3=Test(60)
print("content of t3 :",t3.__dict__)
t4=Test(y=939,x=7282)
print("content of t4 :",t4.__dict__)