'''
Given a string expression representing an expression of fraction addition and subtraction, return the calculation result in string format.

The final result should be an irreducible fraction. If your final result is an integer, change it to the format of a fraction that has a denominator 1. So in this case, 2 should be converted to 2/1.

 

Example 1:

Input: expression = "-1/2+1/2"
Output: "0/1"
Example 2:

Input: expression = "-1/2+1/2+1/3"
Output: "1/3"
Example 3:

Input: expression = "1/3-1/2"
Output: "-1/6"

'''
class Solution:
    # this is the code to find the gcd
    def gcd(self, a, b):
        if a == 0:
            return b
        if b == 0:
            return a
        
        if a == b:
            return a
        
        if a < b:
            return self.gcd(a, b-a)
        
        return self.gcd(a-b, b)
        
    
    def fractionAddition(self, arr: str) -> str:
        num = 0
        den = 1
        neg = False
        i = 0

        while i < len(arr):
            cur_num = 0
            cur_den = 0
            
            if arr[i] == "-":
                neg = True
                i += 1
                continue

            elif arr[i] == "+":
                neg = False
                i += 1
                continue
            
            # this logic is important, need to find numerator first
            while i < len(arr) and arr[i].isdigit():
                cur_num = cur_num*10 + int(arr[i])
                i += 1
            
            i += 1 # skip the /

            # this logic is important, need to find denomenator first
            while i < len(arr) and arr[i].isdigit():
                cur_den = cur_den*10 + int(arr[i])
                i += 1

            if neg:
                cur_num = -1*cur_num

            num = cur_num*den + num*cur_den # this must be before, otherwise den will change
            den = cur_den*den


        # before returing just divide the result, by the gcd
        gcd = self.gcd(abs(den), abs(num))
        
        den = den // gcd
        num = num // gcd
        
        return str(num) + "/" + str(den)
            

            






        