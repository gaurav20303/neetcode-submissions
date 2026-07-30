class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for s in strs:
            t = [0] * 26;
            for i in s:
                t[ord(i)-97] += 1

            t = tuple(t)
            if t in m:
                m[t].append(s)
            else:
                m[t] = [s]

       
        return list(m.values())
            