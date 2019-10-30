class Solution:
    def calculate_area_histogram(self, arr):
        max_area = 0
        stack = []
        for i in xrange(len(arr)):
            if not stack or arr[i] >= arr[stack[-1]]:
                stack.append(i)
            else:
                while stack and arr[stack[-1]] > arr[i]:
                    top = stack[-1]
                    del stack[-1]
                    area = arr[top] * ((i-1-stack[-1]) if stack else i)
                    if area > max_area:
                        max_area = area
                stack.append(i)
        i += 1
        while stack:
            top = stack.pop()
            area = arr[top] * ((i-1-stack[-1]) if stack else i)
            if area > max_area:
                max_area = area

        return max_area
    
    def maximalRectangle(self, arr):
        max_area = 0
        for i in xrange(len(arr)):
            for j in xrange(len(arr[i])):
                if arr[i][j] > 0 and i-1>=0 :
                    arr[i][j] += arr[i-1][j]
            
            _m = self.calculate_area_histogram(arr[i])
            if _m > max_area:
                max_area = _m
        return max_area
    


arr = [  [1, 1, 1],
       [0, 1, 1],
       [1, 1, 0],
    ]

# print(Solution().calculate_area_histogram([5,5,5,5,5]))
print(Solution().maximalRectangle(arr))
