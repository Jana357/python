#program for Demonstrating Default Constructor
#DefaultConstEx1.py
class Test:
	def __init__(self):
		print("i am from Default Constructor:")
		self.a=10
		self.b=20


#main program
t1=Test() # Object Creation--PVM Calls Default Constructor
print("Content of t1=",t1.__dict__)
t2=Test() # Object Creation--PVM Calls Default Constructor
print("Content of t2=",t2.__dict__)
t3=Test() # Object Creation--PVM Calls Default Constructor
print("Content of t3=",t3.__dict__)