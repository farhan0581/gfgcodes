class Solution:
    # @param A : list of integer
    # @param B : integer
    # @return an integer

    def threeSumClosest(self, arr, num):
        arr = sorted(arr)
        # print(arr)
        sum = 0
        mindiff = diff= 99999999999
        _r = None
        for i in range(len(arr)-2):
            p1 = i + 1
            p2 = len(arr)-1

            while p1 < p2:
                sum = (arr[p1]+arr[p2] + arr[i])
                diff = (num - sum)

                # print(diff, mindiff)
                # print('------------')
                if abs(diff) < abs(mindiff):
                    mindiff = diff
                    _r = sum

                if diff == 0:
                    return sum

                elif sum > num:
                    p2 -= 1
                else:
                    p1 += 1
        return _r


print(Solution().threeSumClosest([-20, -1, 1, 5, 5, 16, 18],1)) 
print(Solution().threeSumClosest([2, 1, -9, -7, -8, 2, -8, 2, 3, -8],-1))
print(Solution().threeSumClosest([-4, -8, -10, -9, -1, 1, -2, 0, -8, -2],0))
print(Solution().threeSumClosest([4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8],-3))
# print(Solution().threeSumClosest([ -1, 2, 1, -4],1)) 