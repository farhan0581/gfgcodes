class Solution:
    # @param A : list of integer
    # @param B : integer
    # @return an integer

    def threeSumClosest(self, arr, num):
        arr = sorted(arr)
        sum = 0
        mindiff = diff= 99999999999
        for i in range(len(arr)):
            p1 = 0
            p2 = len(arr)-1

            while p2 >=0 and p1 < len(arr):
                if p2 != p1 and p2 != i and p1 != i:
                    print(arr[i],arr[p1],arr[p2])
                    sum = arr[p1]+arr[p2] + arr[i]
                    diff = sum-num
                    print(diff, mindiff)
                    print('------------')
                    if abs(diff) < abs(mindiff):
                        mindiff = sum

                if diff == 0:
                    return sum
                elif diff > num:
                    p2 -= 1
                else:
                    p1 += 1
                # sum = 0
        return mindiff


# print(Solution().threeSumClosest([-4, -8, -10, -9, -1, 1, -2, 0, -8, -2],0)) 
# print(Solution().threeSumClosest([-4, -8, -10, -9, -1, 1, -2, 0, -8, -2],0)) 
# print(Solution().threeSumClosest([-10,-10,-10],-5)) 
print(Solution().threeSumClosest([ 10, -6, 3, 4, -8, -5],3)) 