
words = input("Enter words separated by space: ").split()

print("Entered words {}".format(words))

palindromes = []

for word in words:
    if word == word[::-1]:
        palindromes.append((word, len(word)))

if palindromes:
    print("Palindrome words and their lengths:")
    for word, length in palindromes:
        print("{} ---> {}".format(word, length))
else:
    print("No palindrome words found.")