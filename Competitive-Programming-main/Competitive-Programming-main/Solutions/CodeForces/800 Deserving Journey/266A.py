n=int(input())
s=input()
c=0
for i in range(len(s)-1):
    if s[i]==s[1+i]:
        c+=1
print(c)