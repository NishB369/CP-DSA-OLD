a,b,c=map(int,input('Enter 3 sides of trianlge as space separated integers: ').split())
if (a+b)>=c or (b+c)>=a or (a+c)>=b:
    print('Legal')
else:
    print('Illegal')