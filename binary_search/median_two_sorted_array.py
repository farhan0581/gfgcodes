class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def find_elem(self, l1, l2, arr1, arr2, i, j):
        # even length
        if (l1+l2)%2 == 0:
            return ((max(arr1[i-1],arr2[j-1]))+min(arr1[i],arr2[j]))/2.0

        # odd length
        else:
            return max(arr1[i-1],arr2[j-1])

    def findMedianSortedArrays(self, lis1, lis2):
        if len(lis2) < len(lis1):
            arr1 = lis2
            arr2 = lis1
        else:
            arr1 = lis1
            arr2 = lis2

        start = 0
        l1 = len(arr1)
        l2 = len(arr2)
        end = l1 if l1 <= l2 else l2
        min_len = end
        i = j = None
        if arr1 and not arr2:
            mid = l1/2
            if l1%2==0:
                return (arr1[mid]+arr1[mid-1])/2.0
            return arr1[mid]
        elif not arr1 and arr2:
            mid = l2/2
            if l2%2==0:
                return (arr2[mid]+arr2[mid-1])/2.0
            return arr2[mid]

        while start <= end:
            i = (start+end)//2 # number of elements in left part
            j = (l1+l2+1)//2 - i # number of elements in right part
            print(i,j)
            # all elements from first array are in right
            if i == 0 and arr2[j-1] <= arr1[i]:
                if (l1+l2)%2==0:
                    return (arr2[j-1]+min(arr1[i],arr2[j]))/2
                else:
                    return arr2[j-1]
            
            # all elements from first array are in left
            if i == min_len and arr1[i-1] <= arr2[j]:
                if (l1+l2)%2==0:
                    return (max(arr1[i-1],arr2[j-1]) + arr2[j])/2
                else:
                    return max(arr1[i-1],arr2[j-1])
   
            
            # print(i,j)
            if i > 0 and arr1[i-1] <= arr2[j] and arr2[j-1] <= arr1[i]:
                return self.find_elem(l1,l2,arr1,arr2,i,j)
   
            # move right in arr1
            elif j > 0 and arr2[j-1] > arr1[i]:
                start = i+1

            # move left in arr1
            elif i > 0 and arr1[i-1] > arr2[j]:
                end = i-1

print(Solution().findMedianSortedArrays([23,26,31,35],[3,5,7,9,11,16]))
print(Solution().findMedianSortedArrays([3,5,10,11,17],[9,13,20,21,23]))
# print(Solution().findMedianSortedArrays([3,5,7,9],[20,21,22,23,24]))
print(Solution().findMedianSortedArrays([-50, -41, -40, -19, 5, 21, 28],[-50, -21, -10 ]))
        


