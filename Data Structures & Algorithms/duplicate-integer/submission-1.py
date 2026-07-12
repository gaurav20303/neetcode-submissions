class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        seen = set()
        i = 0
        while i < n:
            if nums[i] in seen:
                return True
            seen.add(nums[i])
            i += 1

        return False