
n=int(input("enter value u have: "))
if(n<=0):
    print("{} is invalid".format(n))
else:
    lst=list()
    for i in range(1,n+1):
        val=int(input("enter {} value :".format(i)))
        lst.append(val)
    else:
        print("-"*50)
        print("list of values :{}".format(lst))
        print("-"*50)
        pslist=[]
        for val in lst:
            if (val<=0):
                continue
            pslist.append(val)
            sum_ps=sum(pslist)
        else:
            print("-"*50)
            print("list of + val {}".format(pslist))
            print("sum of +ve numbers {}".format(sum_ps))
            print("-"*50)
        nglist=[]
        for val in lst:
            if(val>=0):
                continue
            nglist.append(val)
            sum_ng=sum(nglist)
        else:
            print("-"*50)
            print("list of - val {}".format(nglist))
            print("list of sum of - val {}".format(sum_ng))
            print("-"*50)


print("Program executed successfully")