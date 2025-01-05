from College import College
from university import univ
class Student(College):
    def getstudet(self):
        self.sname=input("Enter student name :")
        self.sno=int(input("Enter Stundent no :"))
        self.crs=input("Enter course :")
    def disstudet(self):
        print("-"*50)
        print("Student Name :".format(self.sname))
        print("Student no :".format(self.sno))
        print("Course :".format(self.crs))
        print("-"*50)
#
# s=Student()
#
# s.getcolldet()
# s.getstudet()
# s.getunidet()
# s.disunidet()
# s.discolldet()
# s.disstudet()
