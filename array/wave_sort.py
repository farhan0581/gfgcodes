class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, arr):
        less = False
        arr = sorted(arr)
        
        i = 0
        l = len(arr)
        while i < l-1:
            # print(arr)
            # print(less, i)
            if less and arr[i] > arr[i+1]:
                t = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = t

            elif not less and  arr[i] < arr[i+1]:
                t = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = t
            
            if less:
                less = False
            else:
                less = True

            i += 1
        return arr

print(Solution().wave([ 5, 1, 3, 2, 4 ]))



