#oddnumgen_whileloop

n=int(input("enter how many numbers you want to generate: "))
if (n<=0):
    print("{} is invalid input : ".format(n))
else:
    print("="*50)
    print("odd number within {}".format(n))
    print("="*50)
    i=1
    while(i<=n):
        print("{}".format(i),end="\t")
        i+=2
    else:
        print("="*50)
