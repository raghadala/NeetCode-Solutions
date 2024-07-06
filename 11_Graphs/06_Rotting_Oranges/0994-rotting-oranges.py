"""
Problem: LeetCode 994 - Rotting Oranges

Key Idea:
The problem is to determine the minimum time needed for all oranges to become rotten, considering that rotten oranges can also infect adjacent fresh oranges in each minute. We can model this problem using Breadth-First Search (BFS), where each minute corresponds to a level of the BFS traversal.

Time Complexity:
- In the worst case, all cells are fresh oranges, and each cell can be visited at most once. Therefore, the BFS traversal has a time complexity of O(m * n), where m is the number of rows and n is the number of columns in the grid.

Space Complexity:
- The space complexity is O(m * n), where m is the number of rows and n is the number of columns in the grid. This is the maximum space required for the BFS queue and visited set.
"""


from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        rotten = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # possible adjacent cells

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    # add the rotten orange coordinates to the queue
                    rotten.append((i, j))
                elif grid[i][j] == 1:
                    # update fresh oranges count
                    fresh += 1
        
        minutes = 0
        while rotten and fresh > 0:
            minutes += 1
            #process all rotten oranges
            for _ in range(len(rotten)):
                x,y = rotten.popleft() #get current rotten cords
                #check adjacent cells
                for dx,dy in directions:
                    new_x, new_y = x + dx, y + dy
                    #check if new cords are out of bounds
                    if new_x < 0 or new_x >= rows or new_y < 0 or new_y >= cols:
                        continue
                    if grid[new_x][new_y] == 0 or grid[new_x][new_y] == 2:
                        continue
                    fresh -= 1
                    grid[new_x][new_y]= 2
                    rotten.append((new_x,new_y)) #add new rotten cords
        return minutes if fresh == 0 else -1
        
