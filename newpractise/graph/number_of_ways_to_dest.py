'''
You are in a city that consists of n intersections numbered from 0 to n - 1 with bi-directional roads between some intersections. The inputs are generated such that you can reach any intersection from any other intersection and that there is at most one road between any two intersections.

You are given an integer n and a 2D integer array roads where roads[i] = [ui, vi, timei] means that there is a road between intersections ui and vi that takes timei minutes to travel. You want to know in how many ways you can travel from intersection 0 to intersection n - 1 in the shortest amount of time.

Return the number of ways you can arrive at your destination in the shortest amount of time. Since the answer may be large, return it modulo 109 + 7.

https://takeuforward.org/data-structure/g-40-number-of-ways-to-arrive-at-destination/

 

Example 1:


Input: n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
Output: 4
Explanation: The shortest amount of time it takes to go from intersection 0 to intersection 6 is 7 minutes.
The four ways to get there in 7 minutes are:
- 0 ➝ 6
- 0 ➝ 4 ➝ 6
- 0 ➝ 1 ➝ 2 ➝ 5 ➝ 6
- 0 ➝ 1 ➝ 3 ➝ 5 ➝ 6


Intuition: Since there can be many paths to reach a destination node from the given source node, in this problem, we have to find all those paths that are the shortest in order to reach our destination. For an easier understanding of this particular problem, we can say that we can divide the problem into partitions such as illustrated below :


From the above picture, we may assume that there will be 3 shortest paths to the destination node. But that may not be the case every time. Let us understand how – We assume the total number of ways in which the destination node is reachable by the shortest possible distance be ways[node] where ‘node’ depicts the destination node and node1, node2 and node3 are the three nodes which act as intermediate nodes that provide shortest paths to the destination. We can say :

ways[node] = ways[node1] + ways[node2] + ways[node3] 
Where, ways[node1], ways[node2], and ways[node3] are the number of shortest paths possible to node1, node2, and node3 respectively from the source node, the sum of which is the total possible shortest paths and that can be hence greater than 3.

Approach:

This problem is based on Dijkstra’s Algorithm where we count all the possible shortest paths from the source to the destination node.

Initial configuration:

Priority Queue: Define a Priority Queue which would contain pairs of the type {dist, node }, where ‘dist’ indicates the currently updated value of the shortest dist taken to reach from source to the current ‘node’.
Distance Array: Define a distance array that would contain the minimum distance from the start node to the current node. If a cell is marked as ‘infinity’ then it is treated as unreachable/ unvisited.
Source Node: Define the start node from where we have to calculate the total number of shortest paths.
Ways Array: Define a ways array which would contain the number of possible shortest ways/paths for each node. Eventually, we would want to return ways[n-1] where n= Number of nodes.
The Algorithm consists of the following steps :

Start by creating an adjacency list, a priority queue that stores the dist-node pairs in the form {dist, node} and a dist array with each node initialized with a very large number ( to indicate that the nodes have not been visited initially). 
In addition to the standard configuration of Dijkstra’s algorithm, we have one more array in this problem by the name ‘ways’ which is initialized to ‘0’ for every node when they’re unvisited (so the number of ways is 0).
Now, we push the start node to the queue along with its distance marked as ‘0’ and ways marked as ‘1’ initially because we’ve just started the algorithm.
Pop the element from the front of the queue and look out for its adjacent nodes.
If the current dist value for a number is better than the previous distance indicated by the distance array, we update the distance in the array and push it to the queue. Now, here side by side we also keep the number of ways to the ‘node’ the same as before.
If the current dist value is the same as the previously stored dist value at the same index, increment the number of ways by 1 at that index.
We repeat the above steps until the queue becomes empty or till we reach the destination.
Return the ways[n-1] modulo 10^9+7 when the queue becomes empty.
Here’s a quick demonstration of the Algorithm’s 1st iteration for example 1 stated above ( all the further iterations would be done in a similar way ) :


https://takeuforward.org/wp-content/uploads/2023/01/Screenshot-2023-01-08-151811.png


APPROACH:
- have to use dijkastras, but only twist is that we have to track count of ways.

when in the distance array, if through some path , we arrive at the same distance,
we omit to append in queueu, but this time we increment the count in the ways matrix
because we can arrive through same distance from different path, so we add the ways in that.

'''
import heapq as hp

class Solution:
    def countPaths(self, n, roads):
        #Your code here
        INF = 999999999
        adj = [[] for i in range(n)]
        ways = [0 for i in range(n)]
        costArr = [INF for i in range(n)]
        mod = 1e15+7

        for road in roads:
            i,j,cost = road
            adj[i].append((j,cost))
            adj[j].append((i, cost))
        
        dest = n-1
        ways[0] = 1
        costArr[0] = 0

        q = [(0,0)]
        hp.heapify(q)

        while len(q) > 0:
            cost, node = hp.heappop(q)

            for _adjNode in adj[node]:
                adjNode,adjCost = _adjNode
                if adjCost+cost < costArr[adjNode]:
                    costArr[adjNode] =  adjCost+cost
                    hp.heappush(q,(adjCost+cost, adjNode))
                    ways[adjNode] = (ways[node]%mod)%mod
                elif adjCost+cost == costArr[adjNode]:
                    ways[adjNode] = ((ways[adjNode]%mod)+(ways[node]%mod))%mod
        
        return int(ways[dest]%mod)




        
        




n=7
# n=6
edges = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
# edges = [[0,5,8],[0,2,2],[0,1,1],[1,3,3],[1,2,3],[2,5,6],[3,4,2],[4,5,2]]

print(Solution().countPaths(n,edges))