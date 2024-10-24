s=input()
ns=''
i=0
while i<len(s):
    if s[i]=='.':
        ns+='0'
        i+=1
    else:
        if s[i+1]=='.':
            ns+='1'
            i+=2
        else:
            ns+='2'
            i+=2
print(ns)