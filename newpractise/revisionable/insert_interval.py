'''
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].



APPRAOCH:

Here 3 cases will arive:
1. when newInterval[0] > interval[1] , just keep it
2. case 2 difficult (here we do the merging part)
3. just append

Awesome solution, thank you. For those struggling with the case 2 if statement on newInterval[1] >= intervals[i][0], an easier way to think about it is you TERMINATE the loop once newInterval[1] is < intervals[i][0].

For example,
{[6,8], [10,12], [15,16], [20,22], [23,24]}
and we need to insert [13,18]

The first while loop will make result = {[6,8], [10,12]}. Then we terminate on [15,16] since 16 is !< 13.
Then the second while loop will compare [13,18] and [15,16] and see if 18 >= 15. Yes, this is true. So we update newInterval to be [13,18]. This part might be confusing, but bear with me. Now we compare [13,18] and [20,22]. Here, 18 >= 20 is NOT true, so we terminate. And then insert into result so result = {[6,8], [10,12], [13,18]}. As I said earlier, the easier way to think about this is that 18 < 20, meaning there is no longer an overlap, and we can now terminate the loop.

This part is more easy to understand, but now since the merge intervals part is over, we can just add [20,22] and [23,24] so result = {[6,8], [10,12], [13,18], [20,22], [23,24]}.

Hope that helped anyone as this part heavily confused me at first as well.

Time complexity - O(N)
space complexity - O(1)


----- summary ------

for case 2 in order to break, we have newInterval[1] < intervals[i][0]
so we take all aprt from above ~(newInterval[1] < intervals[i][0]) = newInterval[1] >= intervals[i][0]


'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        insert = False

        if len(intervals) == 0:
            return [newInterval]

        # left half
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        
        # now we are doing comparisons
        while i < len(intervals) and (intervals[i][0] <=  newInterval[1]):
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        
        res.append(newInterval) # this is the merged part
        
        
        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        return res