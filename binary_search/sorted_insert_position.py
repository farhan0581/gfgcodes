class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, arr, num):

        start = 0
        l = len(arr)-1
        end = l
        f = 0
        while start <= end:
            mid = (start+end)/2
            if arr[mid] == num:
                f=1
                break
            elif num < arr[mid]:
                end = mid-1
            elif num > arr[mid]:
                start = mid+1
        # print(mid,arr[mid])
        ind = mid
        if f==0:
            while ind >=0 and ind<=l:
                if num > arr[ind]:
                    ind+=1
                else:
                    break
        return ind

l = [ 3, 4, 18, 19, 20, 27, 28, 31, 36, 42, 44, 71, 72, 75, 82, 86, 88, 97, 100, 103, 105, 107, 110, 116, 
118, 119, 121, 122, 140, 141, 142, 155, 157, 166, 176, 184, 190, 199, 201, 210, 212, 220, 225, 234, 235, 
236, 238, 244, 259, 265, 266, 280, 283, 285, 293, 299, 309, 312, 317, 335, 341, 352, 354, 360, 365, 368, 
370, 379, 386, 391, 400, 405, 410, 414, 416, 428, 433, 437, 438, 445, 453, 457, 458, 472, 476, 480, 485, 
489, 491, 493, 501, 502, 505, 510, 511, 520, 526, 535, 557, 574, 593, 595, 604, 605, 612, 629, 632, 633, 
634, 642, 647, 653, 654, 656, 658, 686, 689, 690, 691, 709, 716, 717, 737, 738, 746, 759, 765, 775, 778,
 783, 786, 787, 791, 797, 801, 806, 815, 820, 822, 823, 832, 839, 841, 847, 859, 873, 877, 880, 886, 904, 
 909, 911, 917, 919, 937, 946, 948, 951, 961, 971, 979, 980, 986, 993 ]
# print(l.index(904))
l=[1,3,5,6]
print(Solution().searchInsert(l,7))

