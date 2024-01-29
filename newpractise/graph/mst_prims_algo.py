'''

APPRAOCH:
- greedy approach is used in this algo.
- we use minheap here
- first create a adjacency list and visited array
- the main thing is that we have to mark visited not while adding to queuue
  but while consuming from queue after popping.
- if poped node is visited, then it means it was visited earlier due to lesser weight of path, so we can
  safely ignore that.

'''

import heapq as hp
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here  

        edges = []
        s = 0
        q = [(0,0,-1)]
        hp.heapify(q)
        vis = [0 for i in range(V)]

        while len(q) > 0:
            wt,node,pt = hp.heappop(q)
            if vis[node] == 1:
                continue
            vis[node] = 1
            if pt != -1:
                s += wt
                edges.append((pt,node))

            for _adjNode in adj[node]:
                adjNode, awt = _adjNode
                if vis[adjNode] == 0:
                    hp.heappush(q, (awt, adjNode, node))

        return s

adj = [[(1,5),(2,1)],[(2,3),(0,5)],[(0,1),(1,3)]]
print(Solution().spanningTree(3,adj))