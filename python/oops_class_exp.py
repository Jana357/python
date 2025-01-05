#Program for storing Student  Number, name , marks(Instance data members)  and course which is common for all students (Class Level data members)
class Student:
    crs="PY"

#main program
s1=Student()
s2=Student()
print("-"*50)
print("Initial Content of s1 {}",s1.__dict__)
print("Initial Content of s2 {}",s2.__dict__)
#Add Instance Data members to s1 object by reading dynamic data
s1.stno=int(input("Enter 1st student number :"))
s1.stname=input("Enter 1st student name :")
#Add Instance Data members to s2 object by reading dynamic data
s2.stno=int(input("Enter 2nd student number :"))
s2.stname=input("Enter 2nd student name :")
print("-"*50)
print("Content of s1:")
print("\tStudent Number: {}".format(s1.stno))
print("\tStudent Name : {}".format(s1.stname))
print("\tStudent Coures : {}".format(s1.crs))
print("-"*50)
print("Content of s2:")
print("\tStudent Number: {}".format(s2.stno))
print("\tStudent Name : {}".format(s2.stname))
print("\tStudent Coures : {}".format(s2.crs))
print("-"*50)


print("---------OR----------")
print("Content of S1 :")
for dvn,den in s1.__dict__.items():
    print("\t{} : {}".format(dvn,den))
print("Content of S2 :")
for dvn,den in s2.__dict__.items():
    print("\t{} : {}".format(dvn,den))

