class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sum = 0
        res = 0
        prefix_sum = {0:1}
        for i in range(n):
            sum += nums[i]
            if (sum - k) in prefix_sum:
                res += prefix_sum[sum-k]
            
            prefix_sum[sum] = prefix_sum.get(sum,0) + 1 
        return res