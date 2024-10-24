# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print((i,j),end='\t')

# s=input()
# print(s[::-1])

# s=input()
# if s==s[::-1]:
#     print('Palindrome')
# else:
#     print('Not a Palindrome')

# s=input()
# k=int(input())
# print(s[k:]+s[:k])

l=eval(input())
# print(sum(l))

# es=0
# os=0
# for i in range(len(l)):
#     if i&1==0:
#         es+=l[i]
#     else:
#         os+=l[i]
# print(es,os)

# if l==l[::-1]:
#     print('Palindrome')
# else:
#     print('Not')

# for i in range(len(l)-1):
#         print(l[i]+l[1+i])

def func(arr):
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = prefix[i - 1] + arr[i]
    return prefix

