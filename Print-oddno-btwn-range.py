start,end = map(int,input().split())
op = []
for i in range(start+1,end):
    if(i%2!=0):
        op.append(i)
print(*op)
