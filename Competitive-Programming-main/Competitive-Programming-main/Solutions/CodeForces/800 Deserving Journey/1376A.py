t=int(input())
for j in range(t):
    s=input()
    ns=s[0]
    for i in range(1,len(s)-1,2):
        if s[i]==s[i+1]:
            ns+=s[i]
    ns+=s[-1]
    print(ns)