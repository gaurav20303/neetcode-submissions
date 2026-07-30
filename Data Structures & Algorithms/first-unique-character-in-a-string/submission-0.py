class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        m = {}
        t = [0] * n
        for i in range(n):
            if s[i] not in m:
                m[s[i]] = i
            
            t[m[s[i]]] += 1
        print(t)
        for i in range(n):
            if t[i] == 1:
                return i
        return -1

        
        