import math
def func(m):
    p=1
    while p<m:
        p*=2

    a=p//2
    b=p
    if abs(m-a)<=abs(p-m):
        return a
    else:
        return b

n=int(input("Enter a number: "))
if n<=0:
    print("Please enter a positive integer.")
else:
    nearest=func(n)
    print(f"The nearest power of 2 to {n} is: {nearest}")

