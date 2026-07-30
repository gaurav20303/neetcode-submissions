class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        p = 1
        for i in range(1, len(nums)):
            p *= nums[i-1]
            left[i] = p
            
        right = [1] * len(nums)
        right[-1] = left[-1]
        p = 1
        for j in range(len(nums)-2, -1, -1):
            p *= nums[j+1]
            right[j] = left[j] * p
        
        return right