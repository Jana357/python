#for loop / while loop
s1="python"
print("======While Loop======")
i=0
while (i<len(s1)):
    print("\t {}".format(s1[i]))
    i=i+1
print("======For Loop======")
for ch in s1:
    print("\t {}".format(ch))
else:
    print("="*50)
