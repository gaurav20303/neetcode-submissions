class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            t = [0] * 26
            for k in s:
                t[ord(k) - ord('a')] += 1
            key = tuple(t)

            if key in d:
                d[key].append(s)
            else:
                d[key] = [s]

        return list(d.values())
        