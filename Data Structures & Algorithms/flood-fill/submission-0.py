class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = ((0,-1), (-1,0), (0,1), (1,0))
        n = len(image)
        m = len(image[0])

        queue = deque()

        prev = image[sr][sc]
        queue.append((sr,sc))
        while queue:
            print(queue)
            i,j = queue.popleft()
            image[i][j] = color
            
            for dr, dc in directions:
                nr, nc = i+dr, j+dc
                if 0 <= nr < n and 0 <= nc < m:
                    if image[nr][nc] == prev and image[nr][nc] != color:
                        queue.append((nr, nc))

        return image

        