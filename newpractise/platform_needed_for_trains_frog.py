'''
You are given the string croakOfFrogs, which represents a combination of the string "croak" from different frogs, that is, multiple frogs can croak at the same time, so multiple "croak" are mixed.

Return the minimum number of different frogs to finish all the croaks in the given string.

A valid "croak" means a frog is printing five letters 'c', 'r', 'o', 'a', and 'k' sequentially. The frogs have to print all five letters to finish a croak. If the given string is not a combination of a valid "croak" return -1.

 

Example 1:

Input: croakOfFrogs = "croakcroak"
Output: 1 
Explanation: One frog yelling "croak" twice.
Example 2:

Input: croakOfFrogs = "crcoakroak"
Output: 2 
Explanation: The minimum number of frogs is two. 
The first frog could yell "crcoakroak".
The second frog could yell later "crcoakroak".
Example 3:

Input: croakOfFrogs = "croakcrook"
Output: -1
Explanation: The given string is an invalid combination of "croak" from different frogs.


APPROACH:
same as min platform, just keep track of frequency and

check frequncy in order also

'''
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        m = {}

        for i in croakOfFrogs:
            f = m.get(i, 0)
            m[i] = f+1

            # check frequency order
            if not (m.get('c',0) >= m.get('r',0) >= m.get('o',0) >= m.get('a',0) >= m.get('k',0)):
                return -1

        # check the total frequency
        if not (m['c'] == m['r'] == m['o'] == m['a'] == m['k']):
            return -1

        maxfrog = 0
        c = 0

        for i in croakOfFrogs:
            if i == "c":
                c += 1
            elif i == "k":
                c -= 1
            
            maxfrog = max(maxfrog, c)
        
        return maxfrog

        