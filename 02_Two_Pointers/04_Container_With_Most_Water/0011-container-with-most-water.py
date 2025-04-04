"""
Problem: LeetCode 11 - Container With Most Water

Key Idea:
To find the maximum area of water that can be held between two vertical lines, we can use a two-pointer approach. We initialize two pointers, one at the beginning of the input array (left) and the other at the end of the array (right). The area between the two vertical lines is calculated as the minimum of the heights at the two pointers multiplied by the distance between them. We then update the maximum area found so far and move the pointer with the smaller height towards the other pointer. We continue this process until the two pointers meet or cross each other.

Time Complexity:
The time complexity of this solution is O(n), where n is the number of elements in the input array 'height'. The two-pointer approach iterates through the array once, and at each step, we move at least one of the pointers, so we do not revisit any element.

Space Complexity:
The space complexity is O(1) since we are not using any additional data structures that depend on the input size. We only use a constant amount of extra space for the two pointers and other variables.
"""


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            res = max(res, min(heights[l], heights[r]) * (r - l)) #take shortest height
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return res
