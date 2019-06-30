class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, arr):
        arr = sorted(arr)
        # print(arr)
        sum = 0
        mindiff = diff= 99999999999
        _r = {}
        result = []
        for i in range(len(arr)-2):
            p1 = i + 1
            p2 = len(arr)-1

            while p1 < p2:
                sum = (arr[p1]+arr[p2] + arr[i])
                if sum == 0:
                    # print(i,p1,p2)
                    key = "%s_%s_%s" % (arr[i],arr[p1],arr[p2])
                    try:
                        _r[key]
                    except:
                        _r[key] = 1
                        result.append([arr[i],arr[p1],arr[p2]])
                    p2 -= 1
                    p1 += 1
                elif sum > 0:
                    p2 -= 1
                elif sum < 0:
                    p1 += 1
        return result

print(Solution().threeSum([-1,0,1,2,-1,-4]))