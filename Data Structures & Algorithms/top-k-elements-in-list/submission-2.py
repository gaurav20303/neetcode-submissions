class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        print(d)

        rev = {v: k for k, v in d.items()}
        sorted_d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        print(sorted_d)
        ans = []
        for key, val in sorted_d.items():
            ans.append(key)
            k -= 1
            if k == 0:
                break
        return ans
        