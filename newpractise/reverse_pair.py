'''
Example 1:

Input: N = 5, array[] = {1,3,2,3,1)

Output: 2 

Explanation: The pairs are (3, 1) and (3, 1) as from both the pairs the condition arr[i] > 2*arr[j] is satisfied.

Example 2:

Input: N = 4, array[] = {3,2,1,4}

Output: 1

Explaination: There is only 1 pair  ( 3 , 1 ) that satisfy the condition arr[i] > 2*arr[j]


Approach:
The steps are basically the same as they are in the case of the merge sort algorithm. The change will be just in the mergeSort() function:

In order to count the number of pairs, we will keep a count variable, cnt, initialized to 0 beforehand inside the mergeSort().
We will add the numbers returned by the previous mergeSort() calls.
Before the merge step, we will count the number of pairs using a function, named countPairs().
We need to remember that the left half starts from low and ends at mid, and the right half starts from mid+1 and ends at high.
The steps of the countPairs() function will be as follows:

We will declare a variable, cnt, initialized with 0.
We will run a loop from low to mid, to select an element at a time from the left half.
Inside that loop, we will use another loop to check how many elements from the right half can make a pair.
Lastly, we will add the total number of elements i.e. (right-(mid+1)) (where right = current index), to the cnt and return it.
'''


class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums = [1,4,200,6,0,-3]
        nums = [1,3,2,3,1]
        nums = [5,4,3,2,1]
        # nums = [2147483647,2147483647,-2147483647,-2147483647,-2147483647,2147483647]

        x = self.mergesort(0,len(nums)-1,nums, 0)
        print(nums)
        print(x)
    
    
    # count pairs separately
    # /Users/farhankhan/Desktop/gfgcodes/data/reverse_pair.png
    def countPairs(self, low,mid,high,arr):
        i = low
        j = mid+1

        cnt = 0

        # start elements in the array 1 and check in array 2
        # the logic is, if element in array 1 satisfy some range in array 2
        # then the next elements must satisfy those range.
        for i in range(low, mid+1):
            while  j <= high and arr[i] > 2*arr[j]:
                j += 1
            cnt += (j - (mid+1)) # range
        return cnt


    def merge(self, low, mid, high, arr):
        i = low
        j = mid+1

        # use temporary storage for storing the elements
        tmp = []

        cnt = self.countPairs(low, mid, high, arr)

        while i <= mid and j <= high:
            # which ever element is smaller will come to the array first
            # increment the one where the element was smaller
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
        
        return cnt


    def mergesort(self,low,high,arr,cnt):
        # this is important initialisation, else wrong results
        cnt = 0
        if low >= high:
            return cnt
        
        mid = (low+high)//2
        
        # break this into smaller arrays until length of them become 1
        # this then becomes the base condition of the recursion above

        cnt += self.mergesort(low,mid,arr,cnt)
        cnt += self.mergesort(mid+1,high,arr,cnt)
        
        
        # now its time to merge
        cnt += self.merge(low,mid,high,arr)
        return cnt



Solution().reversePairs([])

