class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        repeat = set()
        maxs = 0
        def dfs(i,j):
            if (i < 0 or i == len(grid) or j <0 or j == len(grid[0]) or grid[i][j] == 0 or (i,j) in repeat):
                return 0
            
            repeat.add((i,j))
            return (1+dfs(i+1,j)+dfs(i-1,j)+dfs(i,j-1)+dfs(i,j+1))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                maxs = max(dfs(i,j),maxs)
        
        return maxs