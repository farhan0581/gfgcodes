# https://www.geeksforgeeks.org/largest-rectangle-under-histogram/

class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, arr):
        max_area = 0
        stack = []
        index = 0

        while index < len(arr):

            # if greater then previous element then push
            if not stack or arr[stack[-1]] <= arr[index]:
                stack.append(index)
            
            else:
                while stack and arr[stack[-1]] > arr[index]:
                    top = stack.pop()
                    area = arr[top] * ( (index-1-stack[-1]) if stack else index)
                    if max_area < area:
                        max_area = area
                stack.append(index)
            index += 1
        
        while stack:
            top = stack.pop()
            area = arr[top] * ((index-1-stack[-1]) if stack else index)
            if max_area < area:
                max_area = area

        return max_area
            
# print(Solution().largestRectangleArea([2,1,5,6,2,3]))
print(Solution().largestRectangleArea([5,5,5,5,5]))
print(Solution().largestRectangleArea([2,1,5,6,2,3]))
print(Solution().largestRectangleArea([6, 2, 5, 4, 5, 1, 6]))