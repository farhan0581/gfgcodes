class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, arr1, arr2, arr3):
        p1 = len(arr1)-1
        p2 = len(arr2)-1
        p3 = len(arr3)-1
        s = [None,None,None]
        m = 99999999
        min_diff = 99999999999
        while p1 >= 0 and p2 >= 0 and p3 >= 0:
            s = [arr1[p1],arr2[p2],arr3[p3]]
            cur_diff = max(s)-min(s)
            if min_diff > cur_diff:
                min_diff = cur_diff
            newmax = max(s)
            
            if newmax < m:
                m = newmax
            
            if newmax == arr1[p1]:
                p1 -= 1
            elif newmax == arr2[p2]:
                p2 -= 1
            elif newmax == arr3[p3]:
                p3 -= 1
        
        return min_diff


print(Solution().solve( [ 1, 4, 5, 8, 10 ],[ 6, 9, 10 ],[ 2, 3, 6, 10 ]))
