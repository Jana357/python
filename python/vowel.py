word = input("Enter a word: ")

v_word = word.lower()

vowel_found =0


if 'a' in v_word:
    vowel_found = 1
if 'e' in v_word :
    vowel_found = 1
if 'i' in v_word :
    vowel_found = 1
if 'o' in v_word :
    vowel_found = 1
if 'u' in v_word :
    vowel_found = 1

if vowel_found == 1:
    print("The word {} contains at least one vowel.".format(v_word))
else:
    print("The word {} does not contain any vowels.".format(v_word))
