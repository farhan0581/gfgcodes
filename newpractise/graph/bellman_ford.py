'''
Given a weighted and directed graph of V vertices and E edges, Find the shortest
distance of all the vertex's from the source vertex S. If a vertices can't be reach
from the S then mark the distance as 10^8. Note: If the Graph contains a negative cycle then
 return an array consisting of only -1.

 https://takeuforward.org/data-structure/bellman-ford-algorithm-g-41/


 The bellman-Ford algorithm helps to find the shortest distance from the source node to all other nodes. But, we have already learned Dijkstra's algorithm (Dijkstra's algorithm article link) to fulfill the same purpose. Now, the question is how this algorithm is different from Dijkstra's algorithm.

While learning Dijkstra's algorithm, we came across the following two situations, where Dijkstra's algorithm failed:

- If the graph contains negative edges.
- If the graph has a negative cycle (In this case Dijkstra's algorithm fails to minimize the distance, keeps on running, and goes into an infinite loop. As a result it gives TLE error).

Negative Cycle: A cycle is called a negative cycle if the sum of all its weights becomes negative. The following illustration is an example of a negative cycle:

Bellman-Ford's algorithm successfully solves these problems. It works fine with negative edges as well as it is able to detect if the graph contains a negative cycle. But this algorithm is only applicable for directed graphs. In order to apply this algorithm to an undirected graph, we just need to convert the undirected edges into directed edges like the following:




'''
class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, edges, S):
        #code here
        INF = 100000000

        cost = [INF for i in range(V)]
        cost[S] = 0

        for i in range(V-1):
            for edge in edges:
                src,dst,wt = edge
                # adding cost[src] != INF is important because
                # this tells that source itself is not visited (Relaxed)
                if cost[src] != INF and cost[src]+wt < cost[dst]:
                    cost[dst] = cost[src]+wt
        
        # this last loop for checking negative weight cycle (a cycle with overall sum as negative of weights)
        for edge in edges:
            src,dst,wt = edge
            if cost[src] != INF and cost[src]+wt < cost[dst]:
                return [-1]
        
        return cost



    

E = [[0,1,5],[1,0,3],[1,2,-1],[2,0,1]]
S = 2
V = 3

print(Solution().bellman_ford(V,E,S))