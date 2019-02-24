class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, arr, num):
        p1 = p2 = l = 0

        while p2 < len(arr):
            if arr[p2] != num:
                arr[p1] = arr[p2]
                p1 += 1
                l += 1
            p2 += 1
        # print(l, arr)
        return arr

print(Solution().removeElement([4,1,1,2,1,3,1],10))        
