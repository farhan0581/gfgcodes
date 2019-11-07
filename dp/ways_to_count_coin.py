class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def coinchange2_(self, coins, n):
        arr = [[0 for j in xrange(n+1)] for i in xrange(len(coins))]
        mod = 1000007
        for i in xrange(len(coins)):
            for j in xrange(n+1):
                req_sum = j
                try:
                    prev = arr[i-1][j] % mod
                except:
                    prev = 0
                if req_sum == 0:
                    arr[i][j] = 1
                else:
                    # coin value is more, resort to prev value
                    if coins[i] > req_sum:
                        arr[i][j] = prev
                    else:
                        # with coin
                        remain_sum = req_sum - coins[i]
                        arr[i][j] = (prev + arr[i][remain_sum]) % mod
        return arr[i][j] % mod
    
    def coinchange2(self, coins, n):
        arr = [0 for j in xrange(n+1)]
        mod = 1000007
        for i in xrange(len(coins)):
            for j in xrange(n+1):
                req_sum = j

                if req_sum == 0:
                    arr[j] = 1
                else:
                    # coin value is more, resort to prev value
                    if coins[i] <= req_sum:
                        # with coin
                        remain_sum = req_sum - coins[i]
                        arr[j] = (arr[j] + arr[remain_sum]) % mod
        return arr[j] % mod
        
print(Solution().coinchange2([1,2,5],5))

