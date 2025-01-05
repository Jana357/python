try:
    n=int(input("Enter a number: "))
    fact = 1
    if (n<=0):
        print("Error:Enter only positive numbers")
    else:
        for i in range(1,n+1):
            fact=fact*i

except ValueError:
    print("Dont enter special characters, alnum and string")

else:
    print("---------Else Block-----------")
    print("Factorial of {} is {}".format(n,fact))
    print("------------------------------")
finally:
    print("I am from finally block")