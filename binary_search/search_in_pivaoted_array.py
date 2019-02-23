class Solution:
    # @param A : tuple of integer
    # @param B : integer
    # @return an integer
    def find_pivot(self, arr, start, end):
        mid = (start+end)/2
        # print(arr,start,end,mid)
        if mid+1 < len(arr) and arr[mid] > arr[mid+1]:
            return mid
        elif arr[mid] > arr[end] and mid+1 < len(arr):
            return self.find_pivot(arr, mid, end)
        elif arr[mid] < arr[start]:
            return self.find_pivot(arr, start, mid)

        

    def bsearch(self, arr, start, end, num):
        # start = 0
        # end = len(arr)-1
        while start <= end:
            mid = (start+end)/2
            if arr[mid] == num:
                return mid
            elif num > arr[mid]:
                start = mid+1
            elif num < arr[mid]:
                end = mid-1
        return -1


    def search(self, arr, num):
        l = len(arr)
        start = 0
        end = l-1
        pivot = self.find_pivot(arr, start, end)
        if pivot:
            ind = self.bsearch(arr,0,pivot,num)
            if ind == -1:
                ind = self.bsearch(arr,pivot,end,num)
        else:
            ind = self.bsearch(arr, num)
        return ind


print(Solution().search([10,11,12,0,1,2,3,4,5],1))