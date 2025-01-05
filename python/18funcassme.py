def menu():
    print("-"*50)
    print("\tMenu")
    print("\tArthmetic Operations")
    print("-"*50)
    print("\t1.Addition")
    print("\t2.Subtraction")
    print("\t3.Multiplication")
    print("\t4.Division")
    print("\t5.Modulus Division")
    print("\t6.Exponentiation")
    print("\t7.Exit")
    print("-"*50)

addition=lambda a,b:a+b
subtraction=lambda a,b:a-b
division=lambda a,b:a/b
multi=lambda a,b:a*b
mod_div=lambda a,b:a%b
exponen=lambda a,b:a**b

while(True):
    menu()
    ch=int(input("Enter your choice: "))
    match(ch):
        case 1:
            a=int(input("Enter a :"))
            b=int(input("Enter b :"))
            add=addition(a,b)
            print("Addition of {} and {} is: {}".format(a,b,add))
        case 2:
            a=int(input("Enter a :"))
            b=int(input("Enter b :"))
            sub=subtraction(a,b)
            print("Subtraction of {} and {} is: {}".format(a,b,sub))
        case 3:
            a=int(input("Enter a :"))
            b=int(input("Enter b :"))
            m=multi(a,b)
            print("Multiplication of {} and {} is: {}".format(a,b,m))
        case 4:
            a=int(input("Enter a :"))
            b=int(input("Enter b :"))
            div=division(a,b)
            print("Division of {} and {} is: {}".format(a,b,div))
        case 5:
            a=int(input("Enter a :"))
            b=int(input("Enter b :"))
            mod=mod_div(a,b)
            print("Modulus of {} and {} is: {}".format(a,b,mod))
        case 6:
            a=int(input("Enter a :"))
            b=int(input("Enter b :"))
            exp=exponen(a,b)
            print("Exponentiation of {} and {} is: {}".format(a,b,exp))
        case 7:
            print("Program exit")
            print("Thank you for using this program")
            break
        case _:
            print("Invalid choice {}".format(ch))