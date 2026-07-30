class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in m:
                m[nums[i]] += 1
            else:
                m[nums[i]] = 1

        l = [[] for _ in range(n+1)]
        for x,v in m.items():
            l[v].append(x)

        print(l)

        ans = []
        print(k)
        for i in range(n, 0, -1):
            for t in l[i]:
                ans.append(t)
                k -= 1
                if k == 0:
                    return ans

        return ans