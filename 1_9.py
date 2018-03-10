print("to find sum of integers")
n=int(input("enter no. of terms"))
i=0
a=[int(input()) for i in range(0,n)]
b=int(input("Enter no of terms to be added:"))
i=0
sum=0
while(i<b):
  sum=sum+a[i]
  i=i+1
print("sum of integers:")+str(sum)
