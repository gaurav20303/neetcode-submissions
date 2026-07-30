class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        largest_sum = float('-inf')
        
        for i in range(len(nums)):
            if nums[i] > cur_sum and cur_sum < 0:
                cur_sum = nums[i]
            else:
                cur_sum += nums[i]

            if cur_sum > largest_sum:
                largest_sum = cur_sum
            print(cur_sum)

        return largest_sum