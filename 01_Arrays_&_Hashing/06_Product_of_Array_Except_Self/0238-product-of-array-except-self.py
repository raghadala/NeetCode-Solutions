"""
Problem: LeetCode 238 - Product of Array Except Self

Key Idea:
To solve this problem, we can first calculate the product of all elements to the left of each index and store it in a list. Then, we calculate the product of all elements to the right of each index and update the result list accordingly by multiplying it with the previously calculated left product. In this way, each element in the result list will contain the product of all elements except the one at that index.

Time Complexity:
The time complexity of this approach is O(n), where n is the number of elements in the input list. We perform two passes over the list to calculate the left and right products, and each pass takes O(n) time.

Space Complexity:
The space complexity is O(1) for the output list since we are allowed to return the result in the same list. Therefore, the space complexity is constant, as it does not depend on the size of the input list.
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums) # calculate len of list
        result = [1] * n  # result is initialized to a list with all elements set to 1

        # Calculate the left product of each element
        left_product = 1
        for i in range(n):
            result[i] *= left_product  # Set the current element of the result list to the product of all elements to its left
            left_product *= nums[i]  #updated to include the current element

        # Calculate the right product of each element and update the result list
        right_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]

        return result
