'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Example 1:
https://assets.leetcode.com/uploads/2020/08/28/mat1.jpg

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
'''
class Solution:
    def rotate(self, arr: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # transpose
        p = len(arr)-1
        q = len(arr[0])-1
        for i in range(len(arr)):
            for j in range(i+1):
                arr[i][j],arr[j][i] = arr[j][i],arr[i][j]

        #swap
        for i in range(len(arr)):
            start = 0
            end = len(arr[0])-1
            while start <= end:
                arr[i][start], arr[i][end] = arr[i][end], arr[i][start]
                start += 1
                end -= 1
        
        return arr

        