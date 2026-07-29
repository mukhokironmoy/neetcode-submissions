class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return -1

        m = len(grid)
        n = len(grid[0])

        # Create the days matrix
        days = []
        for i in range(m):
            days.append([float("inf")] * n)
        

        # define the dfs
        def dfs(grid, days, i, j, cur_days):
            if i<0 or j<0 or i>=m or j>=n or grid[i][j] == 0 or cur_days >= days[i][j]:
                return

            days[i][j] = cur_days

            dfs(grid, days, i+1, j, cur_days+1)
            dfs(grid, days, i-1, j, cur_days+1)
            dfs(grid, days, i, j+1, cur_days+1)
            dfs(grid, days, i, j-1, cur_days+1)

        # perform the dfs
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    dfs(grid, days, i, j, 0)

        # count the min days
        min_days = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if days[i][j] == float("inf"):
                        return -1

                    min_days = max(min_days, days[i][j])

        return min_days
        