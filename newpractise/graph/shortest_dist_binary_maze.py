'''
Given a n * m matrix grid where each element can either be 0 or 1. You need to find the shortest distance between a given source cell to a destination cell. The path can only be created out of a cell if its value is 1. 

If the path is not possible between source cell and destination cell, then return -1.

Note : You can move into an adjacent cell if that adjacent cell is filled with element 1. Two cells are adjacent if they share a side. In other words, you can move in one of the four directions, Up, Down, Left and Right. The source and destination cell are based on the zero based indexing. The destination cell should be 1.

Example 1:

Input:
grid[][] = {{1, 1, 1, 1},
            {1, 1, 0, 1},
            {1, 1, 1, 1},
            {1, 1, 0, 0},
            {1, 0, 0, 1}}
source = {0, 1}
destination = {2, 2}
Output:
3
Explanation:
1 1 1 1
1 1 0 1
1 1 1 1
1 1 0 0
1 0 0 1
The highlighted part in the matrix denotes the 
shortest path from source to destination cell.


APPROACH:
- use dijkastras(simple bfs), but no need to use priority queueu because the distance is unit
- if distance is not unit, then we have to use a pq.
'''
class Solution:
    
    def shortestPath(self, grid, source, destination):
        # code here
        INF = 99999999
        distance = [[INF for i in range(len(grid[0]))] for j in range(len(grid))]
        distance[source[0]][source[1]] = 0
        
        q = [[source[0],source[1],0]]
        di = [0,0,1,-1]
        dj = [1,-1,0,0]

        while len(q) > 0:
            ni,nj,d = q.pop(0)

            for ind in range(4):
                i = ni+di[ind]
                j = nj+dj[ind]

                if i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0]) and grid[i][j] == 1:
                    if d+1 < distance[i][j]:
                        distance[i][j] = d+1
                        q.append([i,j,d+1])
        
        res = distance[destination[0]][destination[1]]
        if res == INF:
            return -1
        return res



l =        [[1, 1, 1, 1],
            [1, 1, 0, 1],
            [1, 1, 1, 1],
            [1, 1, 0, 0],
            [1, 0, 0, 1]]
source = [0, 1]
destination = [2, 2]

print(Solution().shortestPath(l,source, destination))