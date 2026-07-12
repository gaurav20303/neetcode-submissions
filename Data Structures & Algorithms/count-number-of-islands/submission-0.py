class Solution:

    
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        traversed = [[0] * m for _ in range(n)]
        print(traversed)
        res = 0

        def check(i, j):
            if i < 0 or j < 0 or i >= n or j >= m:
                return
            if grid[i][j] == "0":
                return
            
            grid[i][j] = "0"

            check(i-1,j)
            check(i,j-1)
            check(i+1,j)
            check(i,j+1)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    res += 1
                    check(i,j)
        return res