class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m1 = [0] * 26
        m2 = [0] * 26

        for i in s:
            m1[ord(i)-97] += 1

        for j in t:
            m2[ord(j)-97] += 1

        return m1 == m2
        