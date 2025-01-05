#vowel_count_forloop
line=input("Enter a line :")
print("number of vowels in {}".format(line))
print("="*50)
nov=0
for ch in line:
    if ch in ['a','e','i','o','u']:
        print("\t {} ".format(ch))
        nov=nov+1
print("number of vowels in {}".format(nov))