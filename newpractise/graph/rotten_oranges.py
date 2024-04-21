class Solution:
    
    def bfs(self, grid, q, vis, fresh):

        maxt = 0
        
        
        
        while len(q) > 0:
            i,j,t = q.pop(0)
            vis[i][j] = 1

            dis = [(0,1),(1,0),(-1,0),(0,-1)]

            for k in range(4):
                di,dj = dis[k]
                ni = i + di
                nj = j + dj

                if ni >= 0 and ni < len(grid) and nj >= 0 and nj < len(grid[0]) and grid[ni][nj] == 1 and vis[ni][nj] == 0:
                    q.append((ni,nj,t+1))
                    fresh -= 1
                    maxt = t+1
                    vis[ni][nj] = 1


        return maxt, fresh
        


    #Function to find minimum time required to rot all oranges. 
    def orangesRotting(self, grid):
        
        q = []
        fresh = 0
        vis = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]
        # this is important, all the rotten oranges are the starting points
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j,0))
                    vis[i][j] = 1
                elif grid[i][j] == 1:
                    fresh += 1
        
        maxt, fresh = self.bfs(grid, q, vis, fresh)

        if fresh > 0:
            return -1
        
        return maxt


        


l =[[0,1,2],[0,1,2],[2,1,1]]
# l = [[2,2,0,1]]
print(Solution().orangesRotting(l))