class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArea(self, arr):
        start = 0
        end = len(arr)-1
        maxarea = 0
        i = 0
        while start <= end:
            h = min(arr[start],arr[end])
            area = h*(end-start)
            # print(area)
            if maxarea < area:
                maxarea = area
            if arr[start] == h:
                start += 1
            else:
                end -= 1

        return maxarea

print(Solution().maxArea([1,5,4,3]))
