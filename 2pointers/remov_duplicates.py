class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, arr):
        p1 = p2 = l = 0

        while p2 < len(arr)-1:
            if arr[p2] != arr[p2+1]:
                arr[p1] = arr[p2]
                p1 += 1
                l += 1
            p2 += 1
        arr[p1] = arr[p2]
        l += 1
        # print(arr)
        return l
            
print(Solution().removeDuplicates([1,1,1,2,3,4,4,5,5]))
print(Solution().removeDuplicates([1,2,3,5]))