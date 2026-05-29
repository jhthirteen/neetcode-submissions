class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            nonlocal grid
            # mark node as visited
            grid[i][j] = '-1'
            # find unmarked neighbors
            directions = [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]
            for d in directions:
                new_i = d[0]
                new_j = d[1]
                # search for in-bounds, unvisited nodes
                if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]) and grid[new_i][new_j] == '1':
                    dfs(new_i, new_j)
            return
        
        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    num_islands += 1
        
        return num_islands