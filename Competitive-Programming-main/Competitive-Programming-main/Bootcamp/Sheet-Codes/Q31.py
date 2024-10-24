def func(m):
    if m==1:
        return 1
    else:
        return(m*func(m-1))

n=int(input('Enter a number: '))
print(func(n))