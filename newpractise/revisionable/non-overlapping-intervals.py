'''
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 

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
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

APPROACH:

1. sort by end time, because we will approach by greedy.
2. similar to max meetings in a room
3. only change is, we do not move prev, till we have something

'''
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        if len(intervals) == 1:
            return 0

        intervals.sort(key=lambda x:x[1])

        prev = intervals[0]
        cnt = 0

        for i in range(1, len(intervals)):
            # this condition means there is no overlapping
            if intervals[i][0] >= prev[1]:
                cnt += 1 # how many non overlaps are there
                prev = intervals[i]
        
        return len(intervals)-cnt-1

   
   

