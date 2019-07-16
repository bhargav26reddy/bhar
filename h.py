n=int(input())
l=list(map(int,input().split()))
z=[]
k=len(l)
for i in range(k):
    if(i==l[i]):
        z.append(l[i])
for i in z:
    print(i,end=" ")
if(len(z)==0):
    print("-1")
