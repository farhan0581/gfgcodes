'''
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

 

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.

we use dp array and consider if a cell can form the bottom of a larger square


'''
import "fmt"
func findMin(a,b,c int) int {

    if a > b {
        a = b
    }

    if a > c {
        a = c
    }

    return a

}
func countSquares(matrix [][]int) int {

    

    m := len(matrix)
    n := len(matrix[0])

    dp := make([][]int, m)
    sum := 0

    for i:=0;i<m;i++ {
        dp[i] = make([]int, n)
        for j:=0;j<n;j++ {
            dp[i][j] = 0
            if matrix[i][j] == 1 {
                if i == 0 || j == 0 {
                    dp[i][j] = 1
                    
                } else {
                    mini := findMin(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                    
                    dp[i][j] = 1 + mini
                    
                }    
            }

            sum += dp[i][j]
            
        }
    }

    // fmt.Println(dp)
    return sum
}