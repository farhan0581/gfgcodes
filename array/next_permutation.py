class Solution:
    # @param A : list of integers
    # @return the same list of integer after modification
    def nextPermutation(self, arr):
        end = last = len(arr)-1
        start = len(arr)-1

        while end-1 >=0:
            if arr[end-1] < arr[end]:
                # print(end,end-1)  
                while start >= end-1:
                    if arr[start] > arr[end-1]:
                        temp = arr[start]
                        arr[start] = arr[end-1]
                        arr[end-1] = temp
                        arr[end:] = reversed(arr[end:])
                        return arr
                    start -= 1
            end -= 1
        return sorted(arr)        

print(Solution().nextPermutation([4,5,3,2,1]))
print(Solution().nextPermutation([3]))