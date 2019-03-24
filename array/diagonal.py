class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, arr):
        l = len(arr[0])
        result = []
        i = 0

        for j in xrange(0, l):
            p = i
            q = j
            temp = []
            while q >= 0 and p < l:
                # print(p,q)
                temp.append(arr[p][q])
                p += 1
                q -= 1
            # print('--------------')
            result.append(temp)

        j = l-1
        for i in xrange(1, l):
            p = i
            q = j
            temp = []
            while q > 0 and p < l:
                # print(p,q)
                temp.append(arr[p][q])
                p += 1
                q -= 1
            # print('--------------')
            
            result.append(temp)
        
        
        return result


print(Solution().diagonal([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
]))