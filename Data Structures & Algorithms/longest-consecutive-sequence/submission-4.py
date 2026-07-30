class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        n = len(nums)
        maxL = 0
        if n == 1:
            return 1
        for i in range(1, n):
            k = nums[i]
            l = 0
            while k in s:
                l += 1
                k -= 1
            if l > maxL:
                maxL = l

        for i in range(1, n):
            k = nums[i]
            l = 0
            while k in s:
                l += 1
                k += 1
            if l > maxL:
                maxL = l
        
        return maxL

        