class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])
        m = len(matrix)
        l = 0
        r = m*n - 1
        print(m, n)
        print(l, r)

        def getXY(val):
            y = val%n
            x = (val-y)//n 
            return x,y
        
        while l <= r:
            mid = l + (r-l)//2
            mid1, mid2 = getXY(mid)
            print(mid1, mid2)
            #break
            if matrix[mid1][mid2] < target:
                l1 = mid1
                l2 = mid2
                l = (l1 * n + l2) + 1
            elif matrix[mid1][mid2] > target:
                r1 = mid1
                r2 = mid2
                r = (r1 * n + r2) - 1
            else:
                return True
        return False