class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n1 = len(s)
        n2 = len(t)
        if n1 != n2:
            return False

        d1 = {}
        d2 = {}
        i = 0
        while i < n1:
            if s[i] in d1:
                d1[s[i]] += 1
            else:
                d1[s[i]] = 0

            if t[i] in d2:
                d2[t[i]] += 1
            else:
                d2[t[i]] = 0
            i += 1

        for i in d1:
            if i not in d2 or d1[i] != d2[i]:
                return False
        return True

            
        