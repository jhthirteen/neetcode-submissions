class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            nonlocal cur_size

            # mark the current node as visited
            cur_size += 1
            grid[i][j] = 0

            # define the possible directions of neighboring nodes
            neighbors = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
            # check for in-bounds neighbors that are not visited
            for new_i, new_j in neighbors: 
                if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]) and grid[new_i][new_j] == 1:
                    dfs(new_i, new_j)
            
        
        # define variables to track the state of cur island size, and max seen 
        max_size = 0
        cur_size = 0

        # iterate through our grid, everytime we encounter a node, start the DFS exploration 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i, j)
                    # after recursion completes, check for new max size and reset the cur area 
                    max_size = max(max_size, cur_size)
                    cur_size = 0
        
        return max_size