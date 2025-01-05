n=int(input("Enter how many prime numbers you have: "))
if(n<=0):
    print("{} is invalid".format(n))
else:
    lst=list()
    for i in range(1,n+1):
        val=int(input("Enter {} value:".format(i)))
        lst.append(val)
    else:
        print("-" * 50)
        print("List of values :{}".format(lst))
        print("-" * 50)
        prime = []
        non_prime = []
        for num in lst:
            res = "PRIME"
            for i in range(2, num):
                if (num % i == 0):
                    res = "NOTPRIME"
                    break
            if (res == "PRIME"):
                prime.append(num)
            else:
                non_prime.append(num)

print("Prime numbers :{}".format(prime))
print("Non-prime numbers :{}".format(non_prime))

