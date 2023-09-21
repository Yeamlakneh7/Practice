class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        negative = 0
        col = len(grid[0]) 
        row = len(grid) 
        for i in range(row):
            for j in range(col):
                if grid[i][j] < 0:
                    negative += 1
        return negative
