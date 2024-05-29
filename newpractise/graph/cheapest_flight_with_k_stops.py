from typing import List
import heapq as hq

'''
There are n cities and m edges connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from the city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

 

Note: The price from city A to B may be different From price from city B to A. 
Example 1:
Input:
n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1
Output:
700
Explanation:
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.


APPROACH:
- Its little different because we have to consider hops also, so we make hop as 
  criteria of the minheap, because its better to first go on a route where stops are less.


'''

class Solution:
    def CheapestFLight(self,n,flights,src,dst,k):
        INF = 99999999999
        adj = [[] for i in range(n)]
        for flight in flights:
            i,j,cost = flight
            adj[i].append((j,cost))
        
        
        q = [(0,src,0)]
        hq.heapify(q)

        costArr = [INF for i in range(n)]
        minCost = INF

        while len(q) > 0:
            # print(q)
            hop,node,cost = hq.heappop(q)
            
            # this is not required
            if node == dst:
                if cost < minCost:
                    minCost = cost
            

            for adjNode in adj[node]:

                if hop <= k and adjNode[1]+cost < costArr[adjNode[0]]: # this condition is needed, else TLE
                    costArr[adjNode[0]] = adjNode[1]+cost
                    hq.heappush(q, (hop+1, adjNode[0], cost+adjNode[1]))
            
        if minCost == INF:
            return -1
        return minCost


n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1
print(Solution().CheapestFLight(n, flights, src,dst,k))
