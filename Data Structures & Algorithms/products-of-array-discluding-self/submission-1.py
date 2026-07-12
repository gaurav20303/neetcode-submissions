class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_s = []
        s = 1
        n = len(nums)
        for i in nums:
            left_s.append(s)
            s *= i

        r = 1
        for i in range(n):
            left_s[n-i-1] = left_s[n-i-1] * r
            r *= nums[n-i-1]
        
        return left_s