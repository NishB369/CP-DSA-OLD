l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
nl=[x for x in l1 if x in l2]
print([i for i in l1 if i not in nl]) #A-B = A - (A int B)