class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq = [[] for _ in range(n+1)]
        m = {}
        for i in range(n):
            if nums[i] in m:
                m[nums[i]] += 1
            else:
                m[nums[i]] = 1
        print(m)

        for ke in m.keys():
            freq[m[ke]].append(ke)
        
        print(freq)
        ans = []
        for i in range(n, 0, -1):
            print(k)
            if k == 0:
                break
            for j in freq[i]:
                ans.append(j)
                k -= 1
        return ans