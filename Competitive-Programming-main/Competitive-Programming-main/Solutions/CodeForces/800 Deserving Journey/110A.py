n=int(input())
c=0
for i in str(n):
    if len(str(n))>1 and i in '74':
        c+=1
if c==4 or c==7:
    print("YES")
else:
    print("NO")