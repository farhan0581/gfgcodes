'''
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

'''


class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        vis = [[0 for i in range(n)] for i in range(m)]
        res = grid


        q = []

        # collect all the boundary 1 in the queue

        if m == 1:
            for j in range(n):
                if grid[0][j] == 1:
                    q.append([i,j])
        if n == 1:
            for i in range(m):
                if grid[i][0] == 1:
                    q.append([i,j])
            
        if m > 1 and n > 1:

            for i in [0, m-1]:
                for j in range(n):
                    if grid[i][j] == 1:
                        q.append([i,j])
                        vis[i][j] == 1
                        
            
            for j in [0, n-1]:
                for i in range(1, m-1):
                    if grid[i][j] == 1:
                        q.append([i,j])
                        vis[i][j] == 1
        
                        

        while len(q) > 0:
            i,j = q.pop(0)
            vis[i][j] = 1
            res[i][j] = 2

            for ind in range(4):
                ni = i + di[ind]
                nj = j + dj[ind]

                if ni >= 0 and ni < m and nj >= 0 and nj < n and vis[ni][nj] == 0 and grid[ni][nj] == 1:
                    q.append([ni,nj])
                    vis[ni][nj] = 1
        
        c = 0
        for i in range(m):
            for j in range(n):
                if res[i][j] == 1:
                    c += 1
    
        return c



l = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
print(Solution().numEnclaves(l))
        