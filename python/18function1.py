def menu():
    print("="*50)
    print("\tList Of Figures")
    print("="*50)
    print("\t1.Circle")
    print("\t2.Rectangle")
    print("\t3.Square")
    print("\t4.Exit")
    print("="*50)
circlearea=lambda r: 3.14*r**2
rectarea= lambda l,b:l*b
squarearea=lambda s:s**2

while(True):
    menu()
    choice=int(input("Enter your choice: "))
    match(choice):
        case 1:
            r=float(input("Enter radius: "))
            ca=circlearea(r)
            print("Area of circle {}".format(ca))
        case 2:
            l=float(input("Enter length: "))
            b=float(input("Enter breadth: "))
            ra=rectarea(l,b)
            print("Area of rect {}".format(ra))
        case 3:
            s=float(input("Enter side: "))
            sa=squarearea(s)
            print("Area of square {}".format(sa))
        case 4:
            print("Program exit")
            print("Thank you")
            break