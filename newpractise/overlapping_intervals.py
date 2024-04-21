'''
Given a collection of Intervals, the task is to merge all of the overlapping Intervals.

Example 1:

Input:
Intervals = {{1,3},{2,4},{6,8},{9,10}}
Output: {{1, 4}, {6, 8}, {9, 10}}
Explanation: Given intervals: [1,3],[2,4]
[6,8],[9,10], we have only two overlapping
intervals here,[1,3] and [2,4]. Therefore
we will merge these two and return [1,4],
[6,8], [9,10].
Example 2:

Input:
Intervals = {{6,8},{1,9},{2,4},{4,7}}
Output: {{1, 9}}
Your Task:
Complete the function overlappedInterval() that takes the list N intervals as input parameters and returns sorted list of intervals after merging.

Expected Time Complexity: O(N*Log(N)).
Expected Auxiliary Space: O(Log(N)) or O(N).

Constraints:
1 ≤ N ≤ 100

0 ≤ x ≤ y ≤ 1000


assume the first element is in the array, then start comparing it with the others
if its greater than shrink it, otherwise append it


'''


class Solution:
    def overlappedInterval(self, arr):
        if len(arr) == 1 or len(arr) == 0:
            return arr
        arr.sort(key=lambda x:x[0])
        res = [arr[0]]
        i = 1
        
            
        for i in range(1,len(arr)):
            end = res[-1][1]
            
            if end >= arr[i][0]: # equality condition is important
                res[-1][1] = max(end, arr[i][1])
            else:
                res.append([arr[i][0], arr[i][1]])
            i += 1
                
        
# 		print(res)
        return res