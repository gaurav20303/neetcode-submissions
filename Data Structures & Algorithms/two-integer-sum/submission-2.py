class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        h = {}
        for i in range(n):
            
            j = target-nums[i]
            if j in h and i != h[j]:
                return [h[j], i]
            h[nums[i]] = i
