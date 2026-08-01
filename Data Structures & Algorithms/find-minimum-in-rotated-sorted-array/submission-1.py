class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        n = len(nums)
        l = 0
        r = n-1

        while l < r:
            mid = l + (r-l)//2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            
            if nums[mid] > nums[r]:
                l = mid
            else:
                r = mid

        return nums[0]