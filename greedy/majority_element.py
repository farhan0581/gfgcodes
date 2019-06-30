# https://www.geeksforgeeks.org/majority-element/
# moores alsorithm
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, arr):

        count = 1
        index = 0
        prev = arr[0]

        for i in xrange(len(arr)):
            
            if arr[index] == arr[i]:
                count += 1
                # index = i
            else:
                count -= 1
            
            if count == 0:
                index = i
                count = 1

        # if count == 0:
        #     return arr[-1]
        return arr[index]

print(Solution().majorityElement([ 1, 1, 1, 2, 2 ]))
print(Solution().majorityElement([ 2, 1,  2 ]))
