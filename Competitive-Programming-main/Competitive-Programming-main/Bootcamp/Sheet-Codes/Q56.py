n=int(input('Enter a number: '))
l=[]
for i in range(2,n+1):
    flag=True
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            flag=False
    if flag:
        l.append(i)
print(l)