c=input()
s2=input().strip()
s = "qwertyuiopasdfghjkl;zxcvbnm,./"
ans = ""
for i in s2:
    index = s.find(i)
    if c == 'R':
        ans += s[index - 1]
    else:
        ans += s[index + 1]

print(ans)
