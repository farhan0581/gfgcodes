class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1,4,200,6,0,-3]
        self.mergesort(0,5,nums)
        print(nums)

    def merge(self, low,mid,high,arr):
        i = low
        j = mid+1

        # use temporary storage for storing the elements
        tmp = []

        while i <= mid and j <= high:
            # which ever element is smaller will come to the array first
            if arr[i] > arr[j]:
                tmp.append(arr[j])
                j += 1
            else:
                tmp.append(arr[i])
                i += 1
                
    
        # remaining elements comes to the end
        while i <= mid:
            tmp.append(arr[i])
            i += 1

        # remaining elements comes to the end
        while j <= high:
            tmp.append(arr[j])
            j += 1


        # important here because
        # there is difference in the between the index of the tmp and original array
        # you have to normalize it.
        i = low
        while i <=high:
            arr[i] = tmp[i-low]
            i += 1




    def mergesort(self,low,high,arr):

        if low >= high:
            return
        
        mid = (low+high)//2
        
        # break this into smaller arrays until length of them become 1
        # this then becomes the base condition of the recursion above

        self.mergesort(low,mid,arr)
        self.mergesort(mid+1,high,arr)
        
        # now its time to merge
        self.merge(low,mid,high,arr)



Solution().reversePairs([])

