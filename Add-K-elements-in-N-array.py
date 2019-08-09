n,k = map(int,input().split())
a = [int(x) for x in input().split()][:n]
i=0
sum=0
while(i<k):
    sum=sum+a[i]
    i=i+1
print(sum)
