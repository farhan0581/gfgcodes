'''
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

/Users/farhankhan/Desktop/gfgcodes/data/xogrid.jpg


The approach is to first start BFS with the boundary nodes.
Anything that touches the boundary O will not be covered, so we need to find the other O which
are connected by the boundary O

'''

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        vis = [[0 for i in range(n)] for i in range(m)]
        res = [["X" for i in range(n)] for i in range(m)]

        q = []

        # collect all the boundary O in the queue

        if m == 1:
            for j in range(n):
                if board[0][j] == "O":
                    q.append([i,j])
        if n == 1:
            for i in range(m):
                if board[i][0] == "O":
                    q.append([i,j])
            
        if m > 1 and n > 1:

            for i in [0, m-1]:
                for j in range(n):
                    if board[i][j] == "O":
                        q.append([i,j])
                        vis[i][j] == 1
                        
            
            for j in [0, n-1]:
                for i in range(1, m-1):
                    if board[i][j] == "O":
                        q.append([i,j])
                        vis[i][j] == 1
                    
        

        di = [1,-1,0,0]
        dj = [0,0,-1,1]

        while len(q) > 0:
            i,j = q.pop(0)
            
            vis[i][j] = 1
            res[i][j] = "O"


            for ind in range(4):
                ni = i + di[ind]
                nj = j + dj[ind]
                if ni < m and nj < n and ni >= 0 and nj >= 0:
                    # print(ni,nj,i,j)
                    if vis[ni][nj] == 0 and board[ni][nj] == "O":
                        q.append([ni,nj])
                        vis[ni][nj] = 1
        
        for i in range(m):
            for j in range(n):
                board[i][j] = res[i][j]
        
        print(board)



        


l = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
l = [["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]]
Solution().solve(l)