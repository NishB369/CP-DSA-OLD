l=int(input('Enter the lenght: '))
b=int(input('Enter the breadth: '))

for i in range(b):
    for j in range(l):
        if (i==0 or i==b-1) or ((i!=0 and i!=b-1) and (j==0 or j==l-1)):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()