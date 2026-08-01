class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1
        
        pivot = 0
        while l<r:
            #print(l, r)
            mid = l + (r-l)//2
            if nums[mid] > nums[mid+1]:
                pivot = mid+1
                break
            if nums[mid] > nums[r]:
                l = mid
            else:
                r = mid
            

        print(pivot)

        if target == nums[pivot]:
            return pivot
        l = 0
        r = pivot-1
        
        while l <= r:
            mid = l + (r-l)//2
            if target > nums[mid]:
                l = mid+1
            elif target < nums[mid]:
                r = mid-1
            else:
                return mid

        l = pivot
        r = n-1
        
        while l <= r:
            mid = l + (r-l)//2
            if target > nums[mid]:
                l = mid+1
            elif target < nums[mid]:
                r = mid-1
            else:
                return mid
            

        return -1
