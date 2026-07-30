class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        print(intervals)
        ans = [intervals[0]]
        n = len(intervals)
        for i in range(1, n):
            if intervals[i][0] <= ans[-1][1]:
                if intervals[i][1] > ans[-1][1]:
                    ans[-1][1] = intervals[i][1]
            else:
                ans.append(intervals[i])


        return ans
        