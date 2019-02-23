'''
Integers in each row are sorted from left to right.
The first integer of each row is greater than or equal to the last integer of the previous row.
'''
class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def bsearch(self, arr, num):
        start = 0
        end = len(arr) - 1
        while start <= end:
            mid = (start+end)/2
            if arr[mid] == num:
                return 1
            elif num < arr[mid]:
                end = mid-1
            elif num > arr[mid]:
                start = mid + 1
        return 0

    def searchMatrix(self, arr, num):
        for lis in arr:
            if num <= lis[-1]:
                return self.bsearch(lis, num)
        return 0

print(Solution().searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 11))