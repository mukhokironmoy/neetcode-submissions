class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        m = len(grid)
        n = len(grid[0])

        def dfs(grid, i, j):
            if i<0 or j<0 or i>=m or j>=n or grid[i][j] == "0":
                return

            grid[i][j] = "0"

            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
            dfs(grid, i, j+1)
            dfs(grid, i, j-1)

        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(grid, i, j)
                    islands += 1

        return islands