# https://www.geeksforgeeks.org/find-three-closest-elements-from-given-three-sorted-arrays/
class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, arr1, arr2, arr3):
        i = j = k = 0
        ind_i = ind_j = ind_k = 0
        mindiff = 99999999

        while i < len(arr1) and j < len(arr2) and k < len(arr3):
            minimum = min(arr1[i], arr2[j], arr3[k])
            maximum = max(arr1[i], arr2[j], arr3[k])

            diff = maximum - minimum
            if mindiff > diff:
                ind_i = i
                ind_j = j
                ind_k = k
                mindiff = diff
            
            if arr1[i] == minimum:
                i += 1
            elif arr2[j] == minimum:
                j +=1
            else:
                k += 1
        return max(abs(arr1[ind_i] - arr2[ind_j]), abs(arr2[ind_j] - arr3[ind_k]), abs(arr3[ind_k] - arr1[ind_i]))

print(Solution().minimize([1, 4, 10],[2, 15, 20],[10, 12]))
