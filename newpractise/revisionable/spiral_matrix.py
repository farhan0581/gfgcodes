class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r = len(matrix)
        c = len(matrix[0])
        cnt = r*c
        res = []
        i = 0

        left = 0
        right = c-1
        bottom = r-1
        top = 0
        
        
        while len(res) < r*c:
            
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top += 1

            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right, left-1, -1):
                    res.append(matrix[bottom][i])
                
                bottom -= 1

            if left <= right:
                for i in range(bottom, top-1, -1):
                    res.append(matrix[i][left])
                left += 1
        
        return res
            
        