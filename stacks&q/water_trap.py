class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, arr):
        left = []
        right = []
        start = 0
        end = len(arr)-1

        while start < len(arr):
            if left and arr[start] > left[-1]:
                left.append(arr[start])
            else:
                if not left:
                    left.append(arr[start])
                else:
                    left.append(left[-1])

            if right and arr[end] > right[-1]:
                right.append(arr[end])
            else:
                if not right:
                    right.append(arr[end])
                else:
                    right.append(right[-1])
            start += 1
            end -= 1
        
        right = right[::-1]
        
        total_area = 0

        for index, val in enumerate(arr):
            area = min(left[index], right[index]) - arr[index]
            total_area += area
        return total_area
        

print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])) 
