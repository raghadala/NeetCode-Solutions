"""
Problem: LeetCode 252 - Meeting Rooms

Key Idea:
We can solve this problem by sorting the intervals based on their start times and then checking for any overlapping intervals. If the start time of the current interval is less than the end time of the previous interval, it means there is an overlap, and the person cannot attend all meetings. Otherwise, there is no overlap, and the person can attend all meetings.

Time Complexity:
- The time complexity of this approach is O(n log n) due to the sorting step, where n is the number of intervals.

Space Complexity:
- The space complexity is O(1), as we use only a constant amount of extra space.
"""


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True

        # Sort intervals by their start times (first element of each interval)
        intervals.sort(key=lambda x: x.start)

        for i in range(1, len(intervals)):
            # If the start time of the current interval is less than the end time of the previous 
            if intervals[i].start < intervals[i - 1].end:
                return False

        return True

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)

        for i in range(1,len(intervals)):
            i1 = intervals[i]
            i2 = intervals[i-1]
            if i1.start < i2.end:
                return False
        return True
