#User function Template for python3
from typing import List
import heapq as hq

class Solution:
    def shortestPath(self,n, m, edges):
        # code here
        INF = 9999999999
        cost = [INF for i in range(n+1)]
        cost[1] = 0
        parent = [i for i in range(n+1)]
        
        adj = [[] for i in range(n+1)]
        
        for edge in edges:
            u,v,c = edge
            adj[u].append((v,c))
            adj[v].append((u,c))
        
        q = [(0, 1)]
        
        hq.heapify(q)
        
        while len(q) > 0:
            dis, node = hq.heappop(q)
            if node == n:
                reach = True
            
            for _adjNode in adj[node]:
                adjNode, _dis = _adjNode
                if cost[adjNode] > cost[node] + _dis:
                    cost[adjNode] = cost[node] + _dis
                    hq.heappush(q, (cost[adjNode], adjNode))
                    parent[adjNode] = node
        
        
                    
        res = []
        i = n
        
        if cost[n] == INF:
            return [-1]
        
        while True:
            if parent[i] == i:
                break
            res.append(i)
            i = parent[i]
        
        res.append(1)
        res = [cost[n]] + res[::-1]
        return res