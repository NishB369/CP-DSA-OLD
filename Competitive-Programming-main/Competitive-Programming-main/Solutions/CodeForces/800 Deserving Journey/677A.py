n,h=map(int,input().split())
l=input().split()
w=0
for i in l:
    if int(i)>h:
        w+=2
    else:
        w+=1
print(w)