class Solution:
    def rob(self, nums: List[int]) -> int:
        def collection(n, m={}):
            
            if n == 0:
                m[0] = 0
                return nums[0]
                
            if n == 1:
                m[1] = 1
                return max(nums[0], nums[1])
            if n in m:
                return m[n]
            m[n] = max(nums[n]+collection(n-2),collection(n-1))
            return  m[n]

        return collection(len(nums)-1)