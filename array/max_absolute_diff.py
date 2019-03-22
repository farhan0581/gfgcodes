class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, arr):
        arr1 = []
        arr1 = []

        for index, val in enumerate(arr):
            arr[index] = arr[index] + index
        
        m1 = max(arr)-min(arr)

        for index, val in enumerate(arr):
            arr[index] = arr[index] - 2*index
        
        m2 = max(arr)-min(arr)

        return max(m1,m2)

print(Solution().maxArr([1,2,3,4,5]))