choice='y'
while(choice=='y'):
  a=int(input("check whether it is +ve or -ve:"))
  if(1<=a<=100000):
    print("number is +ve")
  elif (a==0):
    print("number is zero")
  else:
    print("number is -ve")
  choice=input("do you want to continue(y/n)")

