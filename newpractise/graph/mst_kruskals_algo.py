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
class DisJoint:
    def __init__(self, V):
        self.vertices = V
        self.parent = [i for i in range(V+1)]
        self.size = [1 for i in range(V+1)]
        self.rank = [1 for i in range(V+1)]
    
    # ultimate parent
    def ultimate_parent(self, node):
        if node == self.parent[node]:
            return node
        # call recursively and store it
        # this is called path compression 
        self.parent[node] = self.ultimate_parent(self.parent[node])
        return self.parent[node]
        
    # union by size
    def union_by_size(self, u, v):
        ultimate_parent_u = self.ultimate_parent(u)
        ultimate_parent_v = self.ultimate_parent(v)
        if ultimate_parent_u == ultimate_parent_v:
            return False
        
        if self.size[ultimate_parent_u] < self.size[ultimate_parent_v]:
            self.parent[ultimate_parent_u] = ultimate_parent_v
            self.size[ultimate_parent_v] += self.size[ultimate_parent_u]
        else:
            self.parent[ultimate_parent_v] = ultimate_parent_u
            self.size[ultimate_parent_u] += self.size[ultimate_parent_v]
        return True

import heapq as hp
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here

        q= []
        disjoint_set = DisJoint(V)

        for i in range(V):
            for adjNode in adj[i]:
                q.append((adjNode[1],i, adjNode[0]))
        
        hp.heapify(q)

        edges = []
        s = 0

        while len(q) > 0:
            wt,u,v = hp.heappop(q)
            if disjoint_set.union_by_size(u,v):
                edges.append((u,v))
                s += wt
        print(edges)
        return s

adj = [[(1,5),(2,1)],[(2,3),(0,5)],[(0,1),(1,3)]]
print(Solution().spanningTree(3,adj))