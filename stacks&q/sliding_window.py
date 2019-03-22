from collections import deque

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, arr, size):
        result = []
        dq = deque()
        for i in range(size):
            while dq and arr[i] >= arr[dq[-1]]:
                dq.pop()
            dq.append(i)
        
        result.append(arr[dq[0]])
        
        for i in range(size, len(arr)):
            # out of window elements
            while dq and dq[0] <= i - size:
                dq.popleft()
            
            while dq and arr[i] >= arr[dq[-1]]:
                dq.pop()
            dq.append(i)
            result.append(arr[dq[0]])
        
        return result

print(Solution().slidingMaximum([8, 5, 10, 7, 9, 4, 15, 12, 90, 13],4))
