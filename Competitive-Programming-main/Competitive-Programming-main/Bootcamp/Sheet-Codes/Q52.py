def func(n):
    for i in range(1,11):
        print(n,'*',i,'=',n*i,sep='  ')

t=int(input('Enter a number: '))
func(t)