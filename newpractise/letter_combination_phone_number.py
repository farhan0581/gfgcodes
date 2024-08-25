'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

https://assets.leetcode.com/uploads/2022/03/15/1200px-telephone-keypad2svg.png 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
'''
class Solution:
    
    def recur(self, arr, m, tmp, res):
        
        if len(arr) == 0:
            res.append(tmp)
            return


        for char in m[arr[0]]:
            self.recur(arr[1:], m, tmp+char, res)

        return
    
    
    def letterCombinations(self, digits: str) -> List[str]:
        m = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
             "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        res = []
        if digits == "":
            return []
        self.recur(digits, m, "", res)

        return res
            

            
        
        
