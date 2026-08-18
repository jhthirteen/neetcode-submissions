class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        visited = set()

        def dfs(i, j):
            # mark the node as visited
            visited.add((i, j))
            neighbors = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
            # iterate through neighbors, looking for inbounds 1s
            for new_i, new_j in neighbors: 
                if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]) and (new_i, new_j) not in visited and grid[new_i][new_j] == '1':
                    # recursively call dfs
                    dfs(new_i, new_j)
        

        # iterate through the graph, call dfs on any unvisited 1s.
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in visited: 
                    dfs(i, j)
                    # when our base DFS call returns, we've explored an entire island
                    num_islands += 1
        
        return num_islands
