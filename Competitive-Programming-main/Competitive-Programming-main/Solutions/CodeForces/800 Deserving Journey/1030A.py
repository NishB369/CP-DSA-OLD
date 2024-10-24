n = int(input())
l=list(map(int, input().split()))

if sum(l) > 0:
    print("Hard")
else:
    print("Easy")