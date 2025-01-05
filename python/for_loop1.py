#forLoop_num_generator
n=int(input("Enter a number: "))
if(n<=0):
    print("{} is invalid".format(n))
else:
    print("="*50)
    print("the numbers within {}".format(n))
    print("="*50)
    for i in range(1,n+1):
        print("\t {}".format(i),end = " ")
    else:
        print("="*50)