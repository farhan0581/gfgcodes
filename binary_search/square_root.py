class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, num):
        # if num in [0,1]:
        #     return num
        # possible = range(1, (num/2)+1)

        start = 0
        end = num
        # print(possible)
        while start <= end:
            mid = (start+end)/2
            val = mid*mid
            if val == num:
                # print('here')
                return mid

            # move right
            elif val < num:
                start = mid + 1
            # move left
            elif val > num:
                end = mid - 1
        
        # not perfect square
        # print(val, mid, num)
        try:
            if num > val and (mid+1)*(mid+1) < num:
                return mid+1
            elif num < val and (mid-1)*(mid-1) < num:
                return mid-1
        except:
            pass
        return mid

print(Solution().sqrt(8))
