class Solution:
    def replaceDigits(self, s: str) -> str:
        ns=''
        for i in range(len(s)):
            if i%2==0:
                ns+=s[i]
            else:
                ns+=chr(ord(s[i-1])+int(s[i]))
        return ns