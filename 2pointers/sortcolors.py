class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, arr):
        c0 = c1 = c2 = 0
        p1 = 0
        for elem in arr:
            if elem == 0:
                c0 += 1
                arr[p1] = 0
                p1 += 1
            elif elem == 1:
                c1 += 1
            else:
                c2 += 1
        while c1:
            arr[p1] = 1
            p1 += 1
            c1 -= 1
        while c2:
            arr[p1] = 2
            p1 +=1
            c2 -= 1
        return arr

print(Solution().sortColors([1,1,1,1,0,0,0,2,2,2,0,1,2,2,2,2]))