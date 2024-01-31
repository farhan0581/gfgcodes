'''
You are given a graph with n vertices and m edges.

You can remove one edge from anywhere and add that edge between any two vertices in one operation.

Find the minimum number of operations that will be required to make the graph connected.

If it is not possible to make the graph connected, return -1.

 

Example 1: 

Input:
n=4
m=3
Edge=[ [0, 1] , [0, 2] , [1, 2] ]

Output:
1

Explanation:
Remove edge between vertices 1 and 2 and add between vertices 1 and 3.
 

Example 2:

Input:
n=6
m=5
Edge=[ [0,1] , [0,2] , [0,3] , [1,2] , [1,3] ]

Output:
2

Explanation:
Remove edge between (1,2) and(0,3) and add edge between (1,4) and (3,5)


APPROACH:

- we use disjoint set here
- first we find the number of disconnected components.
  how ?
  We check in the parent array, if any node is parent itself, we count it, basically finding number of boses.
- then we find number of extra edges
  we check while doing union by size, if its true it means it required to make it connected
  otherwise its extra node

to make n disconnected components connected we need n-1 extra nodes

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

class Solution:
    def Solve(self, n, edges):
        disjoint_set = DisJoint(n)
        extra_edges = 0
        for edge in edges:
            if not disjoint_set.union_by_size(edge[0], edge[1]):
                extra_edges += 1
        

        disconnected = 0
        for i in range(n):
            if disjoint_set.parent[i] == i:
                disconnected += 1
        
        if extra_edges >= disconnected-1:
            return disconnected-1
        return -1



n=4
edges=[ [0, 1] , [0, 2] , [1, 2] ]
print(Solution().Solve(n,edges))