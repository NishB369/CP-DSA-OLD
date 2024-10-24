n=int(input())
x=input().split()
xl=[int(_) for _ in x]
y=input().split()
yl=[int(_) for _ in y]
nl=list(set(xl[1:]+yl[1:]))
st=set(nl)
if len(st)==n:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')