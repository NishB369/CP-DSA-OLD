l=list(map(int,input().split()))
flag=True
for i in range(2,len(l)):
    if l[i]!=l[i-1]+l[i-2]:
        flag=False
if flag:
    print('Yes, it depicts Fibonnaci sequence.')
else:
    print('No, it doesn\'t depict Fibonnaci sequence.')