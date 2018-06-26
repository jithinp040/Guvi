c=['a','e','i','o','u','A','E','I','O','U']
choice='y'
while(choice=='y'):
  a=str(input("Enter character to check whether vowel or consonant:"))
  if(a in c):
    print("character is vowel")
  else:
    print("character is consonant")
  choice=input("do you want to continue(y/n):")
