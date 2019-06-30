class Solution:
    # @param A : list of integers
    # @return an integer
    def nTriang(self, arr):
        arr = sorted(arr)
        count = 0
        for i in xrange(len(arr)-2):
            j = i + 1
            k = i + 2

            while j < len(arr):
                while k < len(arr):
                    # print(i,j,k)
                    # print('-------------------')
                    if arr[i]+arr[j] > arr[k]:
                        count += 1
                        # print(arr[i],arr[j],arr[k])
                        k += 1
                    else:
                        break
                j +=1
                k = j+1
        return count
                       
print(Solution().nTriang( [4,6,13,16,20,3,1,12]))
print(Solution().nTriang( [1,1,1,2,2]))
            
