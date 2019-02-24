class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, arr1, arr2):
        p1 = p2 = 0
        res = []
        while p1 < len(arr1) and p2 < len(arr2):
            if arr1[p1] == arr2[p2]:
                res.append(arr1[p1])
                p1+=1
                p2+=1
            
            elif arr1[p1] > arr2[p2]:
                p2 += 1
            
            elif arr1[p1] < arr2[p2]:
                p1 += 1
        return res

# print(Solution().intersect([1, 2, 3, 3, 4, 5, 6],[3,3,5]))