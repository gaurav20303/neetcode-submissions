class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        grid = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                # print(row)
                # print(col)
                # print(grid)
                g = int(i/3)*3 + int(j/3)
                if num in row[i] or num in col[j] or num in grid[g]:
                    return False
                row[i].add(num)
                col[j].add(num)
                grid[g].add(num)
                

        return True
                
        