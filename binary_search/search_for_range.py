class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def bsearch(self, arr, num):
        start = 0
        end = len(arr) - 1
        while start <= end:
            mid = (start+end)/2
            if arr[mid] == num:
                return mid
            elif num < arr[mid]:
                end = mid-1
            elif num > arr[mid]:
                start = mid + 1
        return -1

    def searchRange(self, arr, val):
        start = 0
        end = len(arr)-1
        left = right = -1

        mid = self.bsearch()
        if mid != -1:
            left = self.searchRange(arr[0:mid],val)
            right = self.searchRange(arr[mid+1:],val)
            

        # while start <= end:
        #     mid = (start + end)/2
        #     if arr[mid] == val:
                
        #     elif val < arr[mid]:
        #         end = mid-1
        #     elif val > arr[mid]:
        #         start = mid+1
        # return -1
        
        
        
        
        # print(left, right)
        # res = []
        # while True:
        #     if left-1>=0 and val == arr[left-1]:
        #         left = left-1
        #     else:
        #         break
        # while True:
        #     if (right+1)<len(arr) and val == arr[right+1]:
        #         right+=1
        #     else:
        #         break
        # return [left,right]

print(Solution().searchRange([1,1,1,1],1))