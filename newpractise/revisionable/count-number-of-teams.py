'''
There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

 

Example 1:

Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 
Example 2:

Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.
Example 3:

Input: rating = [1,2,3,4]
Output: 4


- Can also do with DP
- below solution works only for a triplet

'''
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0
        # this loop is for the middle element , fix the middle element
        for i in range(1, len(rating)-1):
            leftSmall = leftBig = rightBig = rightSmall = 0
            # find in the left half
            for k in range(0, i):
                if rating[k] < rating[i]:
                    leftSmall += 1
                
                if rating[k] > rating[i]:
                    leftBig += 1
            # find in the right half
            for k in range(i+1, len(rating)):
                if rating[k] < rating[i]:
                    rightSmall += 1
                
                if rating[k] > rating[i]:
                    rightBig += 1
            
            res += leftSmall*rightBig + leftBig*rightSmall
        
        return res