class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1

        pivotIndex = 0
        while l < r:
            
            mid = l + (r - l) // 2
            if l == mid or r == mid:
                pivotIndex = mid
                break
            if nums[l] < nums[mid]:
                l = mid
            elif nums[mid] < nums[r]:
                r = mid
            
        print(pivotIndex)
        
        if nums[0] <= target and target <= nums[pivotIndex]:
            l = 0
            r = pivotIndex
            while l <= r:
                
                mid = l + (r - l) // 2
                if target < nums[mid]:
                    r = mid-1
                elif target > nums[mid]:
                    l = mid+1
                else:
                    return mid

        else:
            print('here')
            l = pivotIndex+1
            r = n - 1
            while l <= r:
                
                mid = l + (r - l) // 2
                print(f'mid: {mid}')
                if target < nums[mid]:
                    r = mid-1
                elif target > nums[mid]:
                    l = mid+1
                else:
                    return mid
        return -1