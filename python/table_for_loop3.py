#forloop_mul_table
n=int(input("enter a number to print table : "))

if n<=0:
    print("{} is invalid".format(n))

else:
    print("="*50)
    print("The number is {}".format(n))
    print("="*50)
    for val in range(1,11):
        print("\t {} * {} = {}".format(val,n,val*n))
    else:
        print("="*50)
