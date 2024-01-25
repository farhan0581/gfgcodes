class Solution:
    def dfs(self, V, adj, vis, color, clr):
        vis[V] = 1
        color[V] = clr

        for adjNode in adj[V]:
            if vis[adjNode] == 0:
                vis[adjNode] = 1
                if not self.dfs(adjNode, adj, vis, color, clr^1):
                    return False
            else:
                if color[adjNode] == clr:
                    return False
        
        return True
    
    def isBipartite(self, V, adj):
        vis = [0 for i in range(V)]
        color = [None for i in range(V)]

        for vertex in range(V):
            if vis[vertex] == 0:
                vis[vertex] = 1
                if not self.dfs(vertex, adj, vis, color, 1):
                    return False
                
        return True
    

l=[[1], [0, 2], [1]]
l = [[2,3],[3],[0,3],[0,1,2]]
v = len(l)
print(Solution().isBipartite(v,l))