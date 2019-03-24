class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, arr):
        mstart = start = end = mend = 0
        sum = msum = 0
        flag = False
        is_positive = 0
        for i in xrange(len(arr)):
            if arr[i] >= 0:
                
                if flag:
                    start = i
                    flag = False

                is_positive = 1
                end = i
                sum += arr[i]
                # print(i,sum, msum)
                if sum > msum:
                    print(sum,msum,mend,mstart,start,end)
                    msum = sum
                    mend = end
                    mstart = start
                elif sum == msum:
                    print('here')
                    print(mstart,mend,start,end)
                    if mend-mstart < end-start:
                        mend = end
                        mstart = start
                    elif mstart > start:
                        mstart = start
                        mend = end
                # print(start, end)
            
            else:
                # print(start, end)
                # mend = end
                # mstart = start
                sum = 0
                flag = True
        
        if not is_positive:
            return []

        return arr[mstart:mend+1]

print(Solution().maxset([ 336465782, -278722862, -2145174067, 1101513929, 1315634022, -1369133069, 1059961393, 628175011, -1131176229, -859484421 ]))
# print(Solution().maxset())