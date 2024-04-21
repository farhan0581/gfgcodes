'''
let x is missing and y is repeating

sum = n*(n+1)/2
product = n*(n+1)*(2n+1)/6

cursum + x - y = sum
curproduct + x2 - y2 = product


'''

#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        
        apr = (n*(n+1)*(2*n+1))//6
        acs = (n*(n+1))/2
        
        s = 0
        p = 0
        
        for i in range(len(arr)):
            s += arr[i]
            p = p + arr[i]*arr[i]
        
        
        s1 = acs-s
        s2 = apr-p
        
        missing = ((s2//s1) + s1)/2
    
        repeating = missing - s1
        
        return int(repeating), int(missing)
        