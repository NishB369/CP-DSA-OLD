t=int(input())
for i in range(t):
    n=int(input())
    if n<=1399:
        print('Division 4')
    elif 1400<=n<=1599:
        print('Division 3')
    elif 1600<=n<=1899:
        print('Division 2')
    else:
        print('Division 1')
        