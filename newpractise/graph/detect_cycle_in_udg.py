'''
here we need to keep the parent node from where we are coming

'''
from typing import List
class Solution:
    
    
    def bfs(self, node, adj, vis):
        
        q = [(node, -1)]
        vis[node] = 1
        
        while len(q) > 0:
            node, parent = q.pop(0)
            
            for adjNode in adj[node]:
                if vis[adjNode] == 0:
                    vis[adjNode] = 1
                    q.append((adjNode, node))
                else:
                    if parent != adjNode:
                        return 1
                    
        return 0
        
    
    def dfs(self, node, adj, vis, parent):
        
        vis[node] = 1
        
            
        for adjNode in adj[node]:
            if vis[adjNode] == 0:
                vis[adjNode] = 1
                if self.dfs(adjNode, adj, vis, node) == 1:
                    return 1
            else:
                if adjNode != parent:
                    return 1
                    
        
        
        return 0
        
        
    
    #Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        #Code bfs here
        vis = [0 for i in range(V)]
#         path = [0 for i in range(V)]
        
        for i in range(V):
            if vis[i] == 0:
                vis[i] = 1
                cycle = self.dfs(i, adj, vis, -1)
                if cycle:
                    return 1
        return 0
