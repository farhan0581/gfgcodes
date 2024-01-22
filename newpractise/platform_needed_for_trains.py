'''
Given arrival and departure times of all trains that reach a railway station. Find the minimum number of platforms required for the railway station so that no train is kept waiting.
Consider that all the trains arrive on the same day and leave on the same day. Arrival and departure time can never be the same for a train but we can have arrival time of one train equal to departure time of the other. At any given instance of time, same platform can not be used for both departure of a train and arrival of another train. In such cases, we need different platforms.
'''

# /Users/ba-00023252/Desktop/gfgcodes/data/platforms.png
class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        dep = sorted(dep)
        arr = sorted(arr)
        
        maxp = 1
        p = 1
        i = 0
        j = 1
        # its like merge sort
        while i < n and j < n:
            
            if dep[i] >= arr[j]:
                p += 1
                j += 1
            else:
                i += 1
                p -= 1
            maxp = max(maxp, p)
        return maxp
            

arr = [900, 945, 955, 1100, 1500, 1800]
dep = [920, 1200, 1130, 1150, 1900, 2000]

print(Solution().minimumPlatform(6,arr,dep))