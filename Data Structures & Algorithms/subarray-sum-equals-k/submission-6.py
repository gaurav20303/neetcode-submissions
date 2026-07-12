class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm = {0:1}
        current_sum = 0
        count = 0
        for num in nums:

            current_sum += num
            
            if (current_sum - k) in hm:
                count += hm[current_sum-k]
            
            hm[current_sum] = hm.get(current_sum, 0) + 1
        return count