class Solution:
    # https://www.interviewbit.com/problems/find-duplicate-in-array/
    # @param A : tuple of integers
    # @return an integer
    # array size n+1 and integers from 1 to n
    def _repeatedNumber(self, arr):

        for index, val in enumerate(arr):
            if arr[abs(val)] < 0:
                return val
            else:
                arr[val] = -arr[val]
        return -1

    def repeatedNumber(self, arr):
        _map = {}
        for index, val in enumerate(arr):
            if _map.get(val, None) == 1:
                return val
            _map[val] = 1

print(Solution().repeatedNumber((4, 4, 1, 2)))