from kvr_exc import kvrmultable,kvrmultable_0
from multable_call import multable

try:
    n=int(input("Enter a number: "))
    res=multable(n)
except kvrmultable:
    print("Error:Dont enter -ve values")
except kvrmultable_0:
    print("Error:Dont enter 0")
except ValueError:
    print("Error:Dont enter alnums,strings and special characters")
else:
    print(res)
finally:
    print("Program Terminated")