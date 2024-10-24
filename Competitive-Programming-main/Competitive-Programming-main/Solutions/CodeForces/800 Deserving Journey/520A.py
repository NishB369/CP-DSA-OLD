n=int(input())
s=input()
c=0
l=[]
for i in range(len(s)):
    if 97<=ord(s[i].lower())<=122:
        l.append(s[i].lower())
if len(set(l))==26:
    print("YES")
else:
    print("NO")