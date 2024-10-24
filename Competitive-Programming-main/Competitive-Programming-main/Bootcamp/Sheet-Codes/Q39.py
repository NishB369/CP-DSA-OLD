import math
r=int(input('Enter the radius of the circle: '))
for i in range(-r,r+1):
    for j in range(-r, r+1):
        if math.sqrt(i**2+j**2)<=r:
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()