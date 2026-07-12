class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)
        if n == 0:
            return 0
        
        ocr = {}
        i = 0
        b = 0
        e = 0
        m = -1
        for i in range(n):
            if s[i] in ocr:
                if ocr[s[i]]+1 < b:
                    pass
                else:
                    b = ocr[s[i]]+1
            ocr[s[i]] = i
            e = i
            print(b,e)
            if e-b+1 > m:
                m = e-b+1
        return m

        