"""
Problem: LeetCode 74 - Search a 2D Matrix

Key Idea:
Since both the rows and columns in the input 2D matrix are sorted, we can treat the matrix as a one-dimensional sorted array and perform binary search to find the target element. We can map the 2D indices to the corresponding index in the 1D array and then apply binary search to locate the target element.

Time Complexity:
The time complexity of this solution is O(log(m*n)), where m is the number of rows and n is the number of columns in the matrix. The binary search process reduces the search space by half in each step.

Space Complexity:
The space complexity is O(1), as no extra space is used other than a few variables to keep track of indices and values.
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, col = len(matrix), len(matrix[0])
        top, bot = 0, rows-1

        while top <=bot:
            row = (top+bot)//2 # calc mid row index
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else: 
                break
        
        if not (top<=bot):
            return False
        
        l,r = 0, col-1
        row = (top+bot)//2
        while l<=r:
            m = (l+r)//2
            if target > matrix[row][m]:
                l = m +1
            elif target < matrix[row][m]:
                r = m - 1
            else: 
                return True 
        return False
        
