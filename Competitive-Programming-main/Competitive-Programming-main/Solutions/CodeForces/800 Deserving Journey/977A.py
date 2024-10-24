a,b=map(int,input().split())
for i in range(b):
    if int(str(a)[len(str(a))-1]) == 0:
        a//=10
    else:
        a-=1
print(a)