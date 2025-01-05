n=int(input("Enter value u have: "))
if(n<=0):
    print("{} is invalid".format(n))
else:
    lst=list()
    for i in range(1,n+1):
        val=int(input("Enter {} value :".format(i)))
        lst.append(val)
    else:
        print("-"*50)
        print("List of values :{}".format(lst))
        print("-"*50)
        for val in lst:
            if (val<=0):
                continue
            print("Mul table for {}".format(val))
            for i in range(1,11):
                print("\t{} X {} ={}".format(val,i,val*i))
            else:
                print("-"*50)
        else:
            print("Program executed successfully")