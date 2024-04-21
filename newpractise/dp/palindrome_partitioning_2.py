'''
Given a string s, partition s such that every 
substring
 of the partition is a 
palindrome
.

Return the minimum cuts needed for a palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
Example 2:

Input: s = "a"
Output: 0
Example 3:

Input: s = "ab"
Output: 1
'''
import "fmt"
func isPalindrome(arr string) bool {

    start := 0
    end := len(arr)-1

    for {
        if start > end {
            break
        }
        if arr[start] != arr[end] {
            return false
        }
        start += 1
        end -= 1
    }
    return true
}

func solve(s string, i int, dp []int) int {
    if i >= len(s) {
        return 0
    }

    if dp[i] != -1 {
        return dp[i]
    }

    var tmp string
    var minCut int
    minCut = 999999999

    for j:=i;j<len(s);j++ {
        tmp += string(s[j])
        if isPalindrome(tmp) {
            cost := 1 + solve(s, j+1, dp)
            if cost < minCut {
                minCut = cost
            }
        }
    }

    dp[i] = minCut
    return minCut

}

func minCut(s string) int {
    dp := make([]int, len(s))
    for i:=0;i<len(dp);i++ {
        dp[i] = -1
    }
    return solve(s, 0, dp)-1
}