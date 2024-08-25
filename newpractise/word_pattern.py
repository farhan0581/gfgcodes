'''
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false



APPRAOCH
A bijection is both onto and one-to-one. The figure below illustrates:

https://assets.leetcode.com/users/images/1fd20734-396d-48ef-b597-d2bab1ef7f4e_1672536501.2541006.jpeg
These conditions for bijectivity are satisfied if and only if the following is true:

The counts of distinct elements in two groups and the count of distinct mappings are all equal.


'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        m = {}

        i = 0
        j = 0

        start = end = 0

        words = s.split(" ")

        if len(words) != len(pattern):
            return False

        wordPattern = {}
        patternWord = {}

        for i in range(len(words)):
            char = wordPattern.get(words[i], -1)
            if char == -1:
                wordPattern[words[i]] = pattern[i]
                patternWord[pattern[i]] = words[i]
            else:
                _word = patternWord.get(char, -1)
                if _word != words[i]:
                    return False
                if char != pattern[i]:
                    return False

        
        # print(wordPattern, patternWord)
        if len(wordPattern) == len(patternWord):
            return True
        return False