'''
You are given an n x n binary grid. A grid is said to be binary if every value in grid is either 1 or 0.

You can change at most one cell in grid from 0 to 1.

You need to find the largest group of connected  1's.

Two cells are said to be connected if both are adjacent to each other and both have same value.

Example 1

Input:
2
1 1
0 1

Output:
4

Explanation:
By changing cell (2,1) ,we can obtain a connected group of 4 1's
1 1
1 1
 

Example 2

Input:
3
1 0 1
1 0 1
1 0 1

Output:
7

Explanation:
By changing cell (3,2) ,we can obtain a connected group of 7 1's
1 0 1
1 0 1
1 1 1
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
    def MaxConnection(self, grid):
        # code here
        di = [1,-1,0,0]
        dj = [0,0,1,-1]
        n = len(grid)
        disjoint_set = DisJoint((n*n)-1)
        
        # here we iterate every node in n*n array
        # and go to its neighbours to do a union by size
        # through this we can get all connected components and their size as well.
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    node = (i*n)+j
                    
                    parent_node = disjoint_set.ultimate_parent(node)
                    for k in range(4):
                        ni = di[k]+i
                        nj = dj[k]+j
                        
                        if ni >= 0 and ni < n and nj >=0 and nj < n and grid[ni][nj] == 1:
                            adjNode = (ni*n) + nj
                            parent_adjNode = disjoint_set.ultimate_parent(adjNode)
                            if parent_node != parent_adjNode:
                                disjoint_set.union_by_size(parent_node, parent_adjNode)
        
        
        # here we check for every 0 and visit its neighbours
        # if they are 1, we add up there size here
        max_size = 0
        for i in range(n):
            for j in range(n):

                if grid[i][j] == 0:
                    node = (i*n)+j
                    parent_node = disjoint_set.ultimate_parent(node)
                    
                    # because the same component can repeat from other direction
                    # so we take a set
                    adj_parents = set()

                    for k in range(4):
                        ni = di[k]+i
                        nj = dj[k]+j
                        
                        if ni >= 0 and ni < n and nj >=0 and nj < n and grid[ni][nj] == 1:
                            adjNode = (ni*n) + nj
                            parent_adjNode = disjoint_set.ultimate_parent(adjNode)
                            adj_parents.add(parent_adjNode)
                    
                    _size = 0
                    for _node in adj_parents:
                        _size += disjoint_set.size[_node]
                    
                    max_size = max(max_size, _size+1)

        # what if there is no 0 in the array ?
        if max_size == 0:
            return max(disjoint_set.size)

        return max_size




l = [[1, 1, 1],[1, 1, 1],[1, 1, 1]]

print(Solution().MaxConnection(l))