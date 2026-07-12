class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        visited = {}
        max_len = 0
        l = 0
        if n < 1:
            return 0
        for i in range(n):
            r = i
            if s[i] in visited:
                if visited[s[i]] >= l:
                    l = visited[s[i]]+1

            if r-l+1 > max_len:
                max_len = r-l+1
            print(max_len)
            visited[s[i]] = i
        return max_len
        