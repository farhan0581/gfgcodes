'''
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Example 1:

heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explaination: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.


APPROACH:
1. we have to keep track of maximum difference found so for in the path,
   so we modify the algo condition : weight = max(difference between cell, previous weight of source)
2. we have to use a priority queue because we need the minimum.
3. rukna kab hai ? 
    jab hamein pq se destination mile , tab rukna hai, kyun ? 
    ye guranteed minimum hai, warna ham yahan se side and up ja sakte hain, but wo pehle se
    hi traverse kar ke aaya hai, tabhi to minimum hai

    for example in a 3X3 matrix, result hoga 2,2

    ab 2,2 jab pq se aayega , maan lo ye minimum nahein hai, tab ham , 1,2 ya 2,1 daal sakte hain,
    but ye wo pehle hi traverse kar ke aa chuka hai, is liye jab pq se 2,2 aaye , wo min hai

'''
import heapq as hq

class Solution:
        
    def MinimumEffort(self, arr):
        ides,jdes = len(arr)-1, len(arr[0])-1
        INF = 9999999999
        distance = [[INF for i in range(len(arr[0]))] for j in range(len(arr))]
        # source
        distance[0][0] = 0

        di = [0,0,1,-1]
        dj = [1,-1,0,0]


        q = [(0,0,0)]
        hq.heapify(q)

        while len(q) > 0:
            w,i,j = hq.heappop(q)

            if i == ides and j == jdes:
                return w

            for ind in range(4):
                ni = i + di[ind]
                nj = j + dj[ind]

                if ni >= 0 and nj >= 0 and ni < len(arr) and nj < len(arr[0]):
                    cost = max(abs(arr[ni][nj]-arr[i][j]),w)
                    if cost < distance[ni][nj]:
                        distance[ni][nj] = cost
                        hq.heappush(q,(cost, ni,nj))
        
        return -1



l=[[1,2,2],[3,8,2],[5,3,5]]
# l=[[1,2,3],[3,8,4],[5,3,5]]
# l=[[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
print(Solution().MinimumEffort(l))