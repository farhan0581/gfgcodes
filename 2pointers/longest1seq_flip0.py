'''
done using sliding window
https://www.geeksforgeeks.org/find-zeroes-to-be-flipped-so-that-number-of-consecutive-1s-is-maximized/
'''


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def maxone(self, arr, m):
        left = right = 0
        maxsize = 0
        count = 0
        mleft = mright = 0

        while right < len(arr):
            if count <= m:
                if arr[right] == 0:
                    count += 1
                right += 1
            
            elif count > m:
                if arr[left] == 0:
                    count -= 1
                left += 1

            winssize = right-left
            if maxsize < winssize and count <= m:
                maxsize = winssize
                mleft = left
                mright = right
        return [i for i in range(mleft, mright)]

print(Solution().maxone([0,0],1))
print(Solution().maxone([1,1,0,1,1,0,0,1,1,1],2))