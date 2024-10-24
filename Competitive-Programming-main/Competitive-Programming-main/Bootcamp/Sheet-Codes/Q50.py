l=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(l[0])):
    s=0
    for j in range(len(l)):
        s+=l[j][i]
    print(s)