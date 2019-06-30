

class Solution:
    # @param A : list of integers
    # @return an integer
    def _removeDuplicates(self, arr):
        p1 = p2 = l = 0
        c = 0
        f = True
        while p2 < len(arr)-1:
            if arr[p2] != arr[p2+1]:
                arr[p1] = arr[p2]
                p1 += 1
                l += 1
                f = True
            elif arr[p2] == arr[p2+1] and f:
                arr[p1] = arr[p2]
                p1+=1
                l+=1
                f = False
                
            p2 += 1
        arr[p1] = arr[p2]
        l += 1
        # print(arr)
        return l
    # more generoc
    def removeDuplicates(self, arr):
        p1 = p2 = l = 0
        c = 0
        while p2 < len(arr)-1:
            if arr[p2] != arr[p2+1]:
                arr[p1] = arr[p2]
                p1 += 1
                l += 1
                c = 0
            elif arr[p2] == arr[p2+1] and c < 1:
                arr[p1] = arr[p2]
                p1+=1
                l+=1
                c += 1
                
            p2 += 1
        arr[p1] = arr[p2]
        l += 1
        print(arr[0:p1+1])
        return l
            
print(Solution().removeDuplicates([1,1,1,2,3,4,5,5,5,6]))
# print(Solution().removeDuplicates([1,2,3,5]))