"""
Problem: LeetCode 33 - Search in Rotated Sorted Array

Key Idea:
The key idea is to perform binary search to find the target element in the rotated sorted array. We compare the middle element with the target and the endpoints of the subarray to determine which part of the array is sorted. Depending on the comparison, we narrow down the search to the sorted part of the array.

Time Complexity:
The time complexity of this solution is O(log n), where n is the number of elements in the input array. Binary search reduces the search space by half in each step.

Space Complexity:
The space complexity is O(1), as no extra space is used other than a few variables to keep track of indices and values.
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            #left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
           
            #right sorted portion        
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
