a=0
b=[]
print("Enter three numbers:")
for a in range(0,3):
  b.append(int(input()))
if(b[0]>=b[1] and b[0]>=b[2]):
  print("no 1 is greatest")
elif(b[1]>=b[2] and b[1]>=b[0]):
  print("no 2 is greatest")
else:
  print ("no 3 is greatest")
