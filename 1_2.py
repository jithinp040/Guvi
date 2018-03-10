choice='y'
while(choice=='y'):
  a=int(input("Enter number to check whether odd or even:"))
  if(a%2==0):
    print("number is even")
  else:
    print("number is odd")
  choice=input("do you want to continue(y/n):")
