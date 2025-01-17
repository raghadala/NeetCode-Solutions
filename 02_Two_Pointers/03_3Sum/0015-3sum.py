"""
Problem: LeetCode 15 - 3Sum

Key Idea:
To find all unique triplets that sum to zero, we can use a three-pointer approach. First, we sort the input array 'nums' in non-decreasing order. Then, we iterate through the array with a fixed first element (i). For each fixed first element, we use two pointers (left and right) to find the other two elements that sum to the negation of the fixed first element. As the array is sorted, we can move these two pointers towards each other to efficiently find all possible triplets.

Time Complexity:
The time complexity of this solution is O(n^2), where n is the number of elements in the input array 'nums'. Sorting the array takes O(nlogn) time, and the two-pointer approach iterates through the array once, performing a linear search for each element.

Space Complexity:
The space complexity is O(1) since we are not using any additional data structures that depend on the input size. We only use a constant amount of extra space for the three pointers and other variables.
"""


def threeSum(nums):
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: #if a is same as previous element, skip, avoid duplicates
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1 
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]: #skip duplicates
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1 # move pointers to look for next answer
        return res

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:  # if first element is greater than 0, break
                break

            if i > 0 and a == nums[i - 1]: #if a is same as previous element, skip, avoid duplicates
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]: # move a
                        l += 1
                        
        return res

