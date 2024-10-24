t=int(input())
d={'Tetrahedron':4,'Cube':6, 'Octahedron':8, 'Dodecahedron':12, 'Icosahedron':20}
Sum=0
for i in range(t):
    s=input()
    Sum+=d[s]
print(Sum)