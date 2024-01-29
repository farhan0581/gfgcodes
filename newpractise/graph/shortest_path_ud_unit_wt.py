'''
You are given an Undirected Graph having unit weight, Find the shortest path from src 
to all the vertex and if it is unreachable to reach any vertex, then return -1 for that vertex.

Example:

Input:
n = 9, m= 10
edges=[[0,1],[0,3],[3,4],[4 ,5]
,[5, 6],[1,2],[2,6],[6,7],[7,8],[6,8]] 
src=0
Output:
0 1 2 1 2 3 3 4 4

'''
class Solution:
    def shortestPath(self, edges, n, m, src):
        # code here
        adj = [[] for i in range(n)]

        for edge in edges:
            i,j = edge[0],edge[1]
            adj[i].append(j)
            adj[j].append(i)
        
        q = [(src, 0)]
        dis = [999999999 for i in range(n)]
        dis[src] = 0

        while len(q) > 0:
            node,d = q.pop(0)


            for adjNode in adj[node]:
                # this is most important step because we dont use visited array
                # without this, infinite loop, only add to queue if its of use
                # this will help to avoid paths which are repeat.
                if d+1 < dis[adjNode]:
                    dis[adjNode] = d+1
                    q.append((adjNode, d+1))


        return dis



l = [[0,1],[0,3],[3,4],[4 ,5] ,[5, 6],[1,2],[2,6],[6,7],[7,8],[6,8]]
n = 9
m = len(l)
src=0 
print(Solution().shortestPath(l,n,m,src))