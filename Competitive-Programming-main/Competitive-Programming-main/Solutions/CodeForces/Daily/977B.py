n=int(input())
s=input()
l=[]
for i in range(len(s)-1):
    l.append(s[i]+s[1+i])


st=list(set(l))
c=[]
for i in st:
    c.append(l.count(i))
    print(st[c.index(max(c))])
