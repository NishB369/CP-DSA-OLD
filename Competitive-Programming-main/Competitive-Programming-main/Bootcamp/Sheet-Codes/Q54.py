l=list(map(int,input('Enter a list of space separated integers: ').split()))
for i in l:
    if l.count(i)==1:
        print(i)