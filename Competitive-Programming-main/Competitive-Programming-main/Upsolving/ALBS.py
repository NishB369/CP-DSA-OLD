# s = '1011010011010101'
# l = list(s)
# n = len(s)
# c = 0

# i = 0
# while i < n-2:
#     if (l[i] == '0' and l[i+2] == '1'):
#         if l[i+1] == '0':
#             c += 1
#             l[i] = '1'
#         else:
#             c += 1
#             l[i+2] = '0'

#     elif l[i] == '1' and l[i+2] == '1':
#         if l[i+1] == '0':
#             c += 0
#         else:
#             c += 1
#             l[i+1] = '0'

#     elif (l[i] == '0' and l[i+2] == '0'):
#         if l[i+1] == '0':
#             c += 1
#             l[i+1] = '1'
#         else:
#             c += 0

#     else:
#         if l[i+1] == '1':
#             c += 1
#             l[i] = '0'
#         else:
#             c += 1
#             l[i+2] = '1'
#     i += 2

# print(l)
# print(c)

t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    c=0
    for i in range(1,n):
        if s[i]==s[i-1]:
            c+=1
    print(c)