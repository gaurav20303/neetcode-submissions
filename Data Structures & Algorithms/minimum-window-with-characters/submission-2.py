class Solution:
    def minWindow(self, s: str, t: str) -> str:
        f1 = {}
        start = 0
        end = 0
        formed = 0
        first = 0
        required = 0
        n = len(s)
        minL = 1000
        
        for i in t:
            if i in f1:
                f1[i] += 1
            else:
                required += 1
                f1[i] = 1
        
        f2 = {}
        for i in range(n):
            if s[i] in f1:
                if s[i] in f2:
                    f2[s[i]] += 1
                else:
                    f2[s[i]] = 1


                if f2[s[i]] == f1[s[i]]:
                    formed += 1
                   

            
            print(f1)
            print(f2)
            print(formed)
            print(start, end)
            while formed == required:
                if i - start + 1 < minL:
                    minL = i - start + 1
                    first = start
                    end = i
                if s[start] in f1:
                    f2[s[start]] -= 1
                    if f2[s[start]] < f1[s[start]]:
                        formed -= 1
                start += 1

        
        if minL == 1000:
            return ""

        return s[first:end+1]