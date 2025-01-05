n=int(input("enter the range :"))
if (n<=0):
    print("{} is invalid input value".format(n))
else:
    print("="*50)
    print("list of primes :")
    print("="*50)
    for num in range(2,n+1):
        res="PRIME"
        for i in range(2,num):
            if (num%i==0):
                res="NOTPRIME"
                break
        if(res=="PRIME"):
                print("\t{}".format(num))
print("="*50)