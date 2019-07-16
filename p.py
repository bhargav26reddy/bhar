n=int(input())
l=list(map(int,input().split()))
z=[]
for i in l:
    if(l.count(i)<=1):
        z.append(i)
for i in z:
    print(i)
