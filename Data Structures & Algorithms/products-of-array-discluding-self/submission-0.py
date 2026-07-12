class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_pass = [1] * n
        pr = 1
        for i in range(n):
            if i == 0:
                continue
            pr *= nums[i-1]
            left_pass[i] *= pr

        print(left_pass)
        pr = 1
        for i in range(n-2, -1, -1):
            pr *= nums[i+1]
            left_pass[i] *= pr

        return left_pass