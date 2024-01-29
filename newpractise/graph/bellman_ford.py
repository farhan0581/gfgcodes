'''
Given a weighted and directed graph of V vertices and E edges, Find the shortest
distance of all the vertex's from the source vertex S. If a vertices can't be reach
from the S then mark the distance as 10^8. Note: If the Graph contains a negative cycle then
 return an array consisting of only -1.

 https://takeuforward.org/data-structure/bellman-ford-algorithm-g-41/

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