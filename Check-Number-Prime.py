GivenInput=int(input())
flag=0
if(GivenInput%2==0):
  print("no")
else:
  for i in range(3,GivenInput,2):
    if(GivenInput%i==0):
      flag=1
      break
  if(flag==1):
    print("no")
  else:
    print("yes")
