"""
Problem: LeetCode 347 - Top K Frequent Elements

Key Idea:
To find the k most frequent elements in the given list, we can use a hash map (dictionary in Python) to keep track of the frequency of each element. We then use a min-heap (priority queue) to keep the k most frequent elements at the top. We traverse the list once to build the frequency map, and then we traverse the map to keep the k most frequent elements in the min-heap.

Time Complexity:
The time complexity of this approach is O(n + k*log(n)), where n is the number of elements in the input list. Building the frequency map takes O(n) time, and inserting k elements into the min-heap takes O(k*log(n)) time.

Space Complexity:
The space complexity is O(n) because we need to store the frequency map of all elements in the input list. Additionally, the min-heap will also have a space complexity of O(n) in the worst case if all elements are unique.

We first count how many times each number appears in the list using a dictionary. Then we use a min-heap to keep track of the k 
numbers with the highest frequencies. For each number and its frequency, we push a tuple (frequency, number) into the heap, and 
if the heap grows larger than k, we remove the smallest frequency. At the end, the heap contains the k most frequent numbers, so 
we extract just the numbers and return them.
"""

import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}
        for num in nums:
            # Take the current count for num (or 0 if it doesn’t exist yet), then add 1
            frequency_map[num] = frequency_map.get(num, 0) + 1

        min_heap = []
        for num, frequency in frequency_map.items():
            heapq.heappush(min_heap, (frequency, num)) # flip order of freq, num because heap order by first element, we want frequency
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        result = []
        for frequency, num in min_heap:
            result.append(num)
        return result




