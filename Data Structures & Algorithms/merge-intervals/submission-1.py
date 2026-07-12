class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        for interval in intervals:
            if len(ans) < 1:
                ans.append(interval)
                continue
            
            prev = ans[-1]
            if interval[0] <= prev[1]:
                prev[1] = max(prev[1],interval[1])
                ans[-1] = prev
            else:
                ans.append(interval)

        return ans