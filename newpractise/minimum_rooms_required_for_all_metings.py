'''
Important
- its like we have some coins coming to us, we keep them, but some coins expire also, that we have to check.

- first sort both the arrival and departure times.
- now start from second index, i = 1
- check if arrival > last departure (its ok, do nothing)
        else: increase the platform

no need to keep track of max

'''
class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        
        start = sorted(arr)
        end = sorted(dep)
        
        j = 0
        n = 1
        
        for i in range(1, len(start)):
            if start[i] <= end[j] :
                n += 1
                
            else:
                j += 1
        
        return n


a =[
  [1, 18],
  [18, 23],
  [15, 29],
  [4, 15],
  [2, 11],
  [5, 13]
]

a = [      [0, 30],
            [5, 10],
            [15, 20]
     ]

a = [
  [7, 10],
  [4, 19],
  [19, 26],
  [14, 16],
  [13, 18],
  [16, 21]
]

a = [900, 1100, 1235]
b = [1000, 1200, 1240]

print(Solution().minimumPlatform(len(a), a,b))