class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def collection(nums, n, m={}):
            if n == 0:
                m[0] = nums[0]
                return nums[0]
            if n == 1:
                m[1] = max(nums[0], nums[1])
                return max(nums[0], nums[1])
            if n in m:
                return m[n]
            m[n] = max(collection(nums, n-2, m)+nums[n], collection(nums, n-1, m))
            return m[n]
        
        nums1 = nums[1:]
        nums2 = nums[:-1]
        return max(collection(nums1, len(nums1)-1, {}), collection(nums2, len(nums2)-1, {}))