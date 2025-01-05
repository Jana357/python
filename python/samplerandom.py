import random as r
alpha = "QAZXSWEDCVFRTGBNHYUJMKILOPzaqxswcdevfrbgtnhymjukilop"
digits = "0987654321"
ss="!@#$%^&*()"
print("="*50)
for i in range(1,6):
    for val in r.sample(alpha+digits+ss,6):
        print(val,end=" ")
    print()
print("-"*50)
for i in range(1,6):
    lst=r.sample(alpha+digits+ss,6)
    s=""
    s=s.join(lst)
    print(s)
print("="*50)

