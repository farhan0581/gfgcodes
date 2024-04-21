'''
Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: arr = [1,15,7,9,2,5,10], k = 3
Output: 84
Explanation: arr becomes [15,15,15,9,10,10,10]
Example 2:

Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
Output: 83
Example 3:

Input: arr = [1], k = 1
Output: 1

regular front partition dp
'''
func solve(arr []int, i int, k int, dp []int) int {
    if i >= len(arr) {
        return 0
    }

    if dp[i] != -1 {
        return dp[i]
    }

    n := i + k
    if n > len(arr) {
        n = len(arr)
    }

    maxi := -999999999
    maxSum := -999999999
    sum := 0
    for j:=i;j<n;j++ {
        if maxi < arr[j] {
            maxi = arr[j]
        }

        sum = maxi*(j-i+1) + solve(arr, j+1, k, dp)
        if sum > maxSum {
            maxSum = sum
        }

    }
    dp[i] = maxSum
    return maxSum
}

func maxSumAfterPartitioning(arr []int, k int) int {
    dp := make([]int, len(arr))
    for i := 0;i < len(arr);i++ {
        dp[i] = -1
    }
    return solve(arr, 0, k, dp)
}