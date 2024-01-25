'''

Given a Directed Acyclic Graph of N vertices from 0 to N-1 and a 2D Integer array(or vector) edges[ ][ ] of length M, where there is a directed edge from edge[i][0] to edge[i][1] with a distance of edge[i][2] for all i.

Find the shortest path from src(0) vertex to all the vertices and if it is impossible to reach any vertex, then return -1 for that vertex.

Approach:
1. Use dfs to find the topological sort
2. Then use 0 as the source node as per the question.The distance will be 0
3. Then start traversing the topo array., one by one compute the following:
    cost[i,j] = min[(cost_to_i + cost from i to j), cost[i,j]]
'''


class Solution:

    def dfs(self, adj, vis, node, topo):
        vis[node] = 1

        for adjNode in adj[node]:
            if vis[adjNode[0]] == 0:
                self.dfs(adj, vis, adjNode[0], topo)
        
        # need to append in the last for topological sort using dfs.
        topo.append(node)
        return


    def shortestPath(self, n,  m , edges):
        vis = [0 for i in range(n)]
        topo = []

        adj = [[] for i in range(n)]
        costArr = [9999999999 for i in range(n)]

        for edge in edges:
            i = edge[0]
            j = edge[1]
            cost = edge[2]
            t = adj[i]
            t.append((j,cost))
            adj[i] = t

        for i in range(n):
            if vis[i] == 0:
                self.dfs(adj,vis, i, topo)



        # source = topo[-1]
        # print(cost)
        costArr[0] = 0

        for node in reversed(topo):
            for adjNode in adj[node]:
                costArr[adjNode[0]] = min((costArr[node] + adjNode[1]), costArr[adjNode[0]])

        for i in range(n):
            if costArr[i] == 9999999999:
               costArr[i] = -1 
        return costArr





n = 6
l = [[0,1,2],[0,4,1],[4,5,4],[4,2,2],[1,2,3],[2,3,6],[5,3,1]]
m = len(l)

print(Solution().shortestPath(n,m,l))
