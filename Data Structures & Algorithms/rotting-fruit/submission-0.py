class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        fresh = 0
        queue = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append((i,j))

        if fresh == 0:
            return 0
        
        minutes = 0
        
        while queue:
            print(queue)
            for _ in range(len(queue)):
                i,j = queue.popleft()
                print(i,j)
                if i+1 < n and grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    queue.append((i+1,j))
                    fresh -= 1 

                if j+1 < m and grid[i][j+1] == 1:
                    grid[i][j+1] = 2
                    queue.append((i,j+1))
                    fresh -= 1

                if i-1 > -1 and grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    queue.append((i-1,j))
                    fresh -= 1
                
                if j-1 > -1 and grid[i][j-1] == 1:
                    grid[i][j-1] = 2
                    queue.append((i,j-1))
                    fresh -= 1
            
            minutes += 1            

        print(fresh)
        
        return -1 if fresh > 0 else minutes-1

        