import sys

print("="*50)
print("\t Area Figures")
print("\t 1.Rectangle")
print("\t 2.Circle")
print("\t 3.Square")
print("\t 4.Triangle")
print("\t 5.Exit")
print("="*50)

ch=int(input("Enter a choice: "))

match(ch):
    case 1:
        l=float(input("Enter a length: "))
        b=float(input("Enter a breadth: "))
        ar=l*b
        print("Area of Rectangle is {}".format(ar))
    case 2:
        r=float(input("Enter a radius: "))
        ca=3.14*r**2
        print("Area of Circle is {}".format(ca))
    case 3:
        s=float(input("Enter a side length: "))
        sq=s*s
        print("Area of Square is {}".format(sq))
    case 4:
        b=float(input("Enter a base: "))
        h=float(input("Enter a height: "))
        tri=0.5*h*b
        print("Area of Triangle is {}".format(tri))
    case 5:
        print("Exit")
        sys.exit()
    case _:
        print("{},You have entered an invalid choice".format(ch))

print("="*50)
