"""
Problem: LeetCode 200 - Number of Islands

Key Idea:
The problem is to count the number of islands in a 2D grid where '1' represents land and '0' represents water. We can solve this problem using Depth-First Search (DFS) algorithm. For each cell that contains '1', we perform DFS to explore all adjacent land cells and mark them as visited by changing their value to '0'. This way, we count each connected component of '1's as a separate island.

Time Complexity:
- In the worst case, we visit each cell in the grid once. Therefore, the time complexity is O(m * n), where m is the number of rows and n is the number of columns in the grid.

Space Complexity:
- The space complexity is O(m * n), where m is the number of rows and n is the number of columns in the grid. This is the maximum space required for the call stack during DFS traversal.
"""
#we use dfs because its better for recursion bfs requires a queue which takes more space

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
            
        row, col = len(grid), len(grid[0])
        islands = 0 

        def dfs(i,j):  #check if out of bounds
            if i < 0 or i >=row or j < 0 or j >= col or grid[i][j] != "1":
                return 
            else:   #check neighboring indices
                grid[i][j] = "0"
                dfs(i+1, j)
                dfs(i,j+1)
                dfs(i-1,j)
                dfs(i,j-1)
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    dfs(i,j)
                    islands += 1
        
        return islands
        
