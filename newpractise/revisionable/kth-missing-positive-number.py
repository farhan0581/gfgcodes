'''
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.

 

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.

'''
class Solution:
    # binary https://www.youtube.com/watch?v=uZ0N_hZpyps
    def findKthPositive(self, arr: List[int], k: int) -> int:

        start = 0
        end = len(arr)-1

        while start <= end:
            mid = (start+end)//2

            missing = arr[mid]-(mid+1)

            if k > missing:
                start = mid+1
            else:
                end = mid-1
        
        return k + end + 1

    # linear
    def _findKthPositive(self, arr: List[int], k: int) -> int:
        # at each position there can be missing number, how to tell ?
        # [2,3,4,7,11] => [1,2,3,4,5] (ideal) , so in ideal case k=5 means 5th number in array
        # but here there are some missing as well
        for i in range(len(arr)):
            if k >= arr[i]:
                k += 1
        
        return k
        