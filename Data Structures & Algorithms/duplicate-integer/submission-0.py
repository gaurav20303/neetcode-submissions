class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        d = {}
        i = 0
        while i < n:
            if nums[i] in d:
                return True
            d[nums[i]] = True
            i += 1

        return False