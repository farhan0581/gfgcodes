'''
Given a boolean 2D matrix grid of size n * m. You have to find the number of distinct 
islands where a group of connected 1s (horizontally or vertically) forms an island. 
Two islands are considered to be distinct if and only if one island is not equal to another
 (not rotated or reflected).


Input:
grid[][] = {{1, 1, 0, 1, 1},
            {1, 0, 0, 0, 0},
            {0, 0, 0, 0, 1},
            {1, 1, 0, 1, 1}}
Output:
3
Explanation:
grid[][] = {{1, 1, 0, 1, 1}, 
            {1, 0, 0, 0, 0}, 
            {0, 0, 0, 0, 1}, 
            {1, 1, 0, 1, 1}}
Same colored islands are equal.
We have 4 islands, but 2 of them
are equal, So we have 3 distinct islands.


We have to count the number of bfs, this gives the number of islands
but for unique islands we have to store the shape of the islands.
for this we store the index during bfs, now the order remains same while traversal , otherwsie this will not work
After that choose the first as base and subtract from others and then compare in the set.


'''


class Solution:
    def bfs(self, arr, vis, i, j, res):
        tmp = []
        q = [[i,j]]
        m = len(arr)
        n = len(arr[0])

        di = [1,-1,0,0]
        dj = [0,0,-1,1]

        while len(q) > 0:
            i, j = q.pop(0)
            # order remains same if traversal is same
            tmp.append([i,j])
            vis[i][j] = 1

            for ind in range(4):
                ni = i + di[ind]
                nj = j + dj[ind]

                if ni >= 0 and ni < m and nj >= 0 and nj < n and arr[ni][nj] == 1 and vis[ni][nj] == 0:
                    q.append([ni,nj])
                    vis[ni][nj] = 1
        
        res.append(tmp)


    def countDistinctIslands(self, grid):
        m = len(grid)
        n = len(grid[0])

        vis = [[0 for i in range(n)] for i in range(m)]
        c = 0
        res = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and vis[i][j] == 0:
                    vis[i][j] = 1
                    self.bfs(grid,vis,i,j,res)
                    c += 1
        

        
        unique = []
        for item in res:
            if len(item) > 0:
                tmp = tuple()
                # choose the first one as the base element to subtract from others
                bi,bj = item[0]
                for i in range(len(item)):
                    item[i] = item[i][0]-bi, item[i][1]-bj
                    tmp += ((item[i][0],item[i][1]),)
                unique.append(tmp)
            else:
                pass



        return len(set(unique))




l = [[1, 1, 0, 1, 1],[1, 0, 0, 0, 0],[0, 0, 0, 0, 1],[1, 1, 0, 1, 1]]
print(Solution().countDistinctIslands(l))

# l = set([(1),(2),])
# print(l,len(l))