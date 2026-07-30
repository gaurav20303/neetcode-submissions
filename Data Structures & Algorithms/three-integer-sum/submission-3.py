class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        #print(nums)
        n = len(nums)
        ans = []
        for i in range(n-2):
            j = i+1
            k = n-1
            target = -nums[i]
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while j < k:
                if nums[j] + nums[k] < target:
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    
                    j += 1
                    k -= 1

                    # Skip duplicate second elements
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    # Skip duplicate third elements
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return ans