class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def _repeatedNumber(self, arr):
        a = b = None
        s = sum(arr)
        for index, val in enumerate(arr):
            cur_val = arr[val-1]
            if cur_val == 0:
                a = val
                break
            else:
                arr[val-1]=0
                
        # print(arr)
        n = len(arr)
        b = (n*(n+1))/2 - s + a
        return a,b
    
    def repeatedNumber(self, arr):
        n = len(arr)
        squares = 0
        for i in arr:
            squares += i*i
        a = b = None
        diff = (n*(n+1))/2 - sum(arr)
        plus = ((n*(n+1)*(2*n+1))/6 - squares)/diff

        a = (diff+plus)/2
        b = a-diff
        return b,a



print(Solution().repeatedNumber([1,2,3,3,5]))
        
