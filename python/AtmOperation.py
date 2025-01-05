from ATMExcept import *
bal = 500.00
def deposit():
    damt=float(input("Enter the Deposit Amt :"))
    if(damt<=0):
        raise DepositError
    else:
        global bal
        bal=bal+damt
        print("Ur Account xxxxxxx234 Credited with Inr :{}".format(damt))
        print("Now Ur Account Bal INR : {}".format(bal))

def withdraw():
    global bal
    wamt=float(input("Enter the Withdraw Amt :"))
    if(wamt<=0):
        raise WithdarwError
    elif((wamt+500)>bal):
        raise InsuffFundError
    else:
        bal=bal-wamt
        print("Ur Account xxxxxxxx123 Debitted with INR : {}".format(wamt))
        print("Now Ur Account Bal INR :{}".format(bal))

def balenq():
    print("Ur Account Bal INR :{}".format(bal))