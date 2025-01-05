#odd number generator within n using for loop
n=int(input("enter how many numbers you want to generate: "))
if (n<=0):
    print("{} is invalid input : ".format(n))
else:
    print("="*50)
    print("Odd number within {}".format(n))
    print("="*50)
    for i in range(1,n,2):
        print("\t {}".format(i))

print("="*50)