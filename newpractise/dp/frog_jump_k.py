class Solution:
    def solve(self,arr,k,i):
        if i == len(arr)-1:
            return 0

        minCost = 99999999999

        for j in range(1,k+1):
            if i+j < len(arr):
                minCost = min(self.solve(arr,k,i+j) + abs(arr[i]-arr[i+j]), minCost)
                
        
        return minCost


    
    def frogJump(self,k,arr):
        return self.solve(arr,k,0)



k=3
l=[40, 10, 20, 70, 80, 10, 20, 70, 80, 60]
l=[10, 30, 40, 50, 20]
print(Solution().frogJump(k,l))