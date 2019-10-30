class Solution:
    # @param A : list of integers
    # @return an integer
    def _candy(self, arr):
        left = [None]*len(arr)
        right = [None]*len(arr)
        j = 0
        i = 0
        while i < len(arr):
            if arr[i] > arr[j]:
                left[i] = left[j] + 1
            elif arr[i] <= arr[j]:
                left[i] = 1
            j = i
            i += 1

        i = j = len(arr)-1
        
        while i >= 0:
            if arr[i] > arr[j]:
                right[i] = right[j] + 1
            elif arr[i] <= arr[j]:
                right[i] = 1
            j = i
            i -= 1
        
        result = 0
        for i in xrange(len(left)):
            c = max(left[i], right[i])
            result += c
        
        return result

    def candy(self, arr):
        res = [1] * len(arr)
        j = 0
        for i in xrange(len(arr)):
            if arr[i] > arr[j]:
                res[i] = res[j] + 1
            elif arr[i] <= arr[j]:
                res[i] = 1
            j = i
        i = j = len(arr)-1

        t = 1
        while i >= 0:
            if arr[i] > arr[j]:
                t += 1
                res[i] = max(res[i], t)
            elif arr[i] <= arr[j]:
                t = 1
                res[i] = max(res[i], t)
            j = i
            i -= 1
        return sum(res)


print(Solution().candy([12,4,3,11,34,34,1,67]))
print(Solution().candy([5,5,4,3,2,1]))
