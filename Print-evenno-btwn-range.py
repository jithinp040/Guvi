i,j=map(int,input().split())
op=[]
for integer in range(i+1,j):
    if(integer%2==0):
        op.append(integer)
print(*op)
