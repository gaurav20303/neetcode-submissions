class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        l1 = len(s)
        l2 = len(t)
        if l1 != l2:
            return False

        m = {}
        h = set()
        for i in range(l1):
            if s[i] not in m:
                m[s[i]] = t[i]
                if t[i] in h:
                    return False
                h.add(t[i])
            else:
                if m[s[i]] != t[i]:
                    return False
        
        return True
        