class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n-2):
            print(i)
            print('inside')
            if i > 0 and nums[i] == nums[i-1]:
                print('continued')
                continue
            target = -nums[i]
            l = i+1
            
            r = n-1
            
            while l < r:
                
                if (nums[l] + nums[r]) < target:
                    print('less')
                    l += 1
                elif (nums[l] + nums[r]) > target:
                    print('more')
                    r -= 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    print('equal')
                    l += 1
                    r -= 1
                    while l<r and nums[l] == nums[l-1]:
                        l+= 1
                    while l<r and nums[r] == nums[r+1]:
                        r-=1

        return ans
        