class Solution(object):
    def checkPalindrome(self, s):
        start = 0
        end = len(s)-1
        while start <= end:
            if s[start] != s[end]:
                return False
            else:
                start += 1
                end -= 1  
        return True

    
    def recur(self, arr, start, res, ans):
        if start >= len(arr):
            ans.append(res[:])
            return

        i = start

        # important to keep length len(arr) otherwise we will get duplicates
        while i < len(arr):
            if self.checkPalindrome(arr[start:i+1]):
                res.append(arr[start:i+1])
                self.recur(arr, i+1, res, ans)
                res.pop()
                # why we pop ?
                # we pop because in the recursion call the res array keeps growing and 
                # appends the palindrome strings, eventually , the last call goes to line 
                # 15 and (aakhri index) phir saare results ham ans array mein append kar dete hain
                # ab resursion rewind hota hai and call pichle function pe jaati hai , tab hamein res array
                # ko khali bhejna hai warna duplicate results anne lagte hain.
            i += 1
        
        return
    
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        self.recur(s, 0, [], result)
        
        return result
        




l = 'aabb'
print(Solution().partition(l))
        