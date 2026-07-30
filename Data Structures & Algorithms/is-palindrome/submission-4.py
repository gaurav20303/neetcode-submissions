class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = ''
        def isAlphaN(ch):
            if (ord('a') <= ord(ch) <= ord('z')) or (ord('0') <= ord(ch) <= ord('9')):
                return True
            return False

        for c in s:
            if (ord('A') <= ord(c) <= ord('Z')):
                    c = chr(ord(c)+32)
            if isAlphaN(c):
                s_new += c
        print(s_new)
        l=0
        r=len(s_new)-1
        while l < r:
            if s_new[l] != s_new[r]:
                return False
            l+=1
            r-=1

        return True