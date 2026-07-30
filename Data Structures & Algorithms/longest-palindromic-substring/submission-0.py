class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            return l+1, r-1

        for i in range(len(s)):

            # for odd cases
            l1, r1 = expand(i, i)
            if r1-l1 > end-start:
                start = l1
                end = r1

            # for even cases
            l2, r2 = expand(i, i+1)
            if r2-l2 > end-start:
                start = l2
                end = r2

        return s[start:end+1]



        
