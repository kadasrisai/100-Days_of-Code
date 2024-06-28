''' Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.'''

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # Sort intervals by their end time
        intervals.sort(key=lambda x: x[1])
        
        # Initialize variables
        end = intervals[0][1]
        count = 1
        
        # Iterate over the rest of the intervals
        for i in range(1, len(intervals)):
            # If the start time of the current interval is greater than or equal to the end time of the previous interval, they don't overlap
            if intervals[i][0] >= end:
                # Update end time to be the end time of the current interval
                end = intervals[i][1]
                # Increment the count of non-overlapping intervals
                count += 1
            # If they overlap, discard the current interval
            # (we don't need to update end time or count)
            # because the previous interval has a smaller end time and a higher priority
            else:
                continue
        
        # The number of intervals to remove is the difference between the total number of intervals and the count of non-overlapping intervals
        return len(intervals) - count