'''
You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.

 

Example 1:

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
Example 2:

Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
Example 3:

Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.
'''
class Solution:
    def compare(self, s1, s2):
        i = j = 0

        if len(s1) != len(s2) + 1: 
            return False
        while i < len(s1):
            if j < len(s2) and s1[i] == s2[j]:
                i += 1
                j += 1
            else:
                i += 1
        
        if i == len(s1) and j == len(s2):
            return True

        
        return False
        


    def longestStrChain(self, words: List[str]) -> int:
        dp = [1]*len(words)
        words.sort(key=len)
        maxi = 1
        for i in range(len(words)):
            for prev in range(i):
                # print(words[i], words[prev],self.compare(words[i], words[prev]))
                if self.compare(words[i], words[prev]) and dp[i] < 1+dp[prev] :
                    dp[i] = 1+dp[prev]
            
            maxi = max(maxi, dp[i])
        # print(words)
        print(dp)
        return maxi


