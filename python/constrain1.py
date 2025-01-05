class Employee:
    def __init__(self):
        print("IM from constructor")
        self.eno=100
        self.ename="Jana"
    # def __init__(self):
    #     print("-"*60)
    #     self.a=10
e=Employee()
print("Employee detailes :",e.__dict__)

# class Employee:
#     def reademployee(self):
#         self.eno=100
#         self.ename="Jana"
#     # def __init__(self):
#     #     print("-"*60)
#     #     self.a=10
# e=Employee()
# print(e.__dict__)
# e.reademployee()
# print(e.__dict__)