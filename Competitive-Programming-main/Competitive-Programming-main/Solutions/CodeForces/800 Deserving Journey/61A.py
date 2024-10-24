n=input()
m=input()
o=''
for i in range(len(n)):
    if n[i]==m[i]:
        o+='0'
    else:
        o+='1'
print(o)
    