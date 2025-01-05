# s="PYTHON"
# for ch in s:
#     print("\t {}".format(ch))
# print("-"*50)
# for ch in s:
#     if(ch=='O'):
#         break
#     else:
#         print(ch)
# else:
#     print("i am from for loop ")
#
# print("other part from program")

s='PYTHON'
i=0
while(i<len(s)):
    print(s[i])
    i=i+1
else:
    print("-"*50)
i=0
while(i<len(s)):
    if(s[i]=='O'):
        break
    else:
        print(s[i])
        i=i+1
else:
    print("-"*50)