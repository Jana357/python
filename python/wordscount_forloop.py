line=input("Enter a line :")
line=line.lower()
print("The sentance is {}:".format(line))
print("="*50)
nov={}
for ch in line:
        if ch in nov:
            nov[ch]+=1
        else:
            nov[ch]=1

for letter,count in nov.items():
    print("\t {} ---> {}".format(letter,count))











