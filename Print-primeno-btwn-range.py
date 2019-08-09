st,ed=map(int,input().split())
PrimeNos=[]
for i in range(st+1,ed):
    flag=0
    for j in range(2,i):
        if(i%j==0):
            flag=1
            break
    if(flag!=1):
        PrimeNos.append(i)
print(*PrimeNos)
