c=['a','e','i','o','u','A','E','I','O','U']
a=str(input())
if(a in c):
    print("Vowel")
elif(a.isalpha()):
    print("Consonant")
else:
    print("Invalid")
