from typing import List

class Solution:
    # We need to keep the items in the stack in the increasing order
    # this approach is basic optimal , find the left and right smallest and then find the area.
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        leftbound = [0]*len(heights)
        rightbound = [0]*len(heights)

        for i in range(len(heights)):
            
            if len(stack) == 0:
                leftbound[i] = 0
            else:
                print(i,stack)
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                
                if stack:
                    leftbound[i] = stack[-1] + 1
                else:
                    leftbound[i] = 0
            
            stack.append(i)
        
        stack = []
        i = len(heights)-1
        while i >= 0:
            print(i)

            if len(stack) == 0:
                rightbound[i] = len(heights)-1
            else:
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                
                if stack:
                    rightbound[i] = stack[-1] - 1
                else:
                    rightbound[i] = len(heights)-1
                
            stack.append(i)
            i -= 1
        
        max_area = 0
        for i in range(len(leftbound)):
            area = (-leftbound[i]+rightbound[i] + 1)*heights[i]
            max_area = max(max_area, area)
        
        print(leftbound, rightbound)

        return max_area
    

    def findleftmax(self, arr):
        left = [0]*len(arr)

        st = []

        for i in range(len(arr)):
            while st and arr[st[-1]] >= arr[i]:
                st.pop()
            
            if st:
                left[i] = st[-1]
            else:
                left[i] = 0
            st.append(i)
        
        return left

    # this is optimal
    def _largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxarea = 0

        for i,ht in enumerate(heights):
            
            while stack and heights[stack[-1]] > ht:
                ind = stack.pop()

                if stack:
                    area = (i-stack[-1]-1)*heights[ind] # here i is rightbound and stack[-1] is leftbound
                else:
                    area = (i)*heights[ind]
                
                maxarea = max(maxarea, area)
            
            stack.append(i)
        
        
        i = len(heights)
        while len(stack) > 0:
            ind = stack.pop()
            if stack:
                area = (i-stack[-1]-1)*heights[ind]
            else:
                area = (i)*heights[ind]
            
            maxarea = max(maxarea, area)


        
        
        return maxarea




            



            



# print(Solution().largestRectangleArea([1,1]))

# print(Solution().largestRectangleArea([5,5,5,5,5]))
print(Solution().largestRectangleArea([2,1,5,6,2,3]))
# print(Solution().largestRectangleArea([6, 2, 5, 4, 5, 1, 6]))

print(Solution().findleftmax([2,1,5,6,2,3]))