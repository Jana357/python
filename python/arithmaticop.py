import sys

print("="*50)
print("Arithmetic operation")
print("\t1.Addition")
print("\t2.Subtraction")
print("\t3.Multiplication")
print("\t4.Division")
print("\t5.Modular Division")
print("\t6.Exponential")
print("\t7.Exit")
print("="*50)

ch=int(input("Enter your choice: "))
match(ch):
    case 1:
        print("We are performing Addition operation")
        a=int(input("Enter first number: "))
        b=int(input("Enter second number: "))
        print("Sum({},{})={}".format(a,b,a+b))
    case 2:
        print("We are performing Subtraction operation")
        a=int(input("Enter first number: "))
        b=int(input("Enter second number: "))
        print("Sub({},{})={}".format(a,b,a-b))
    case 3:
        print("We are performing Multiplication operation")
        a=int(input("Enter first number: "))
        b=int(input("Enter second number: "))
        print("Mul({},{})={}".format(a,b,a*b))
    case 4:
        print("We are performing Division operation")
        a=int(input("Enter first number: "))
        b=int(input("Enter second number: "))
        print("Div({},{})={}".format(a,b,a/b))
    case 5:
        print("We are performing Modular Division operation")
        a=int(input("Enter first number: "))
        b=int(input("Enter second number: "))
        print("Mod({},{})={}".format(a,b,a%b))
    case 6:
        print("We are performing Exponential operation")
        a=int(input("Enter first number: "))
        b=int(input("Enter second number: "))
        print("Exp({},{})={}".format(a,b,a**b))
    case 7:
        print("Exit")
        sys.exit()
    case _:
        print(" {}, your selected wrong choice ".format(ch))

print("="*50)

