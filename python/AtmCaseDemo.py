from ATMMenu import menu
import sys
from ATMExcept import *
from AtmOperation import *
while(True):
    menu()
    try:
        ch=int(input("Enter Ur Choice :"))
        match(ch):
            case 1:
                try:
                    deposit()
                except ValueError:
                    print("Dont enter alnums , strs and symbol for Deposit Amt:")
                except DepositError:
                    print("Dont try to Deposit -ve and 0 Amount")

            case 2:
                try:
                    withdraw()
                except ValueError:
                    print("Dont enter Alnum,strs and Symbols fro WithDraw Amt :")
                except InsuffFundError:
                    print("Ur Account dont have sufficient Fund ")

            case 3:
                balenq()

            case 4:
                print("Thx for this Atm ---- Visit Again")

                sys.exit()

            case _:
                print("ur Selection of Operation is wrong ----- try again")

    except ValueError:
        print("Dont enter strs,alnms and symbols for choice :")


