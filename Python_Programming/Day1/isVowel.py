def isVowel(a):
    if(a.isalpha()):
        if(a in "aeiou"):
            print("Vowel")
        else:
            print("Consonant")
    else:
        print("Not Alphabet")
isVowel("e")