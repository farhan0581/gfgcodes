'''
There are n stones at some integer coordinate points on a 2D plane. Each coordinate point may have at most one stone.

You need to remove some stones. 

A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the maximum possible number of stones that you can remove.

 

Example 1:

Input:
n=6
[[0 0] ,[ 0 1], [1 0] ,[1 2] ,[2 1] ,[2 2]]

Output:
5

Example:
One way to remove 5 stones are
1--[0,0]
2--[1,0]
3--[0,1]
4--[2,1]
5--[1,2]
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
    # consider each row as a node and entire column as a node also
    # so total m+n nodes will be there
    # so we can easily identify the node and then we have to do the union
    # why ?
    # because when the stone is present at a position, it means that
    # both that row and column can be joined which means we can join the two nodes.
    def maxRemove(self, stones, n):
        row = 0
        col = 0
        for stone in stones:
            row = max(row, stone[0])
            col = max(col, stone[1])
        
        row += 1
        col += 1

        disjoint_set = DisJoint(row+col)
        

        unique_nodes = set()

        for stone in stones:
            i,j = stone
            node_row = i
            node_col = j + row
            disjoint_set.union_by_size(node_row, node_col)
            unique_nodes.add(node_row)
            unique_nodes.add(node_col)
        

        comps = 0
        for item in unique_nodes:
            if item == disjoint_set.ultimate_parent(item):
                comps += 1
        
        return n-comps


    # TLE
    # brute force approach, here consider each cell as a node
    # traverse entire row and column and do union
    def _maxRemove(self, stones, n):
        # Code here
        row = 0
        col = 0
        for stone in stones:
            row = max(row, stone[0])
            col = max(col, stone[1])
        
        row += 1
        col += 1

        arr = [[0 for i in range(col)] for i in range(row)]
        disjoint_set = DisJoint(row*col)
        
        for stone in stones:
            i,j = stone
            arr[i][j] = 1
        
        for i in range(row):
            for j in range(col):
                if arr[i][j] == 1:
                    node = (i*row)+j
                    
                    # row
                    for nj in range(col):
                        if arr[i][nj] == 1:
                            adjNode = (row*i)+nj
                            # print(adjNode)
                            if node != adjNode:
                                disjoint_set.union_by_size(node, adjNode)
                    
                    # col
                    for ni in range(row):
                        if arr[ni][j] == 1:
                            adjNode = (row*ni)+j
                            # print(adjNode)
                            if node != adjNode:
                                disjoint_set.union_by_size(node, adjNode)
        


            # print(disjoint_set.parent, disjoint_set.size)
        components = 0
        for i in range(row):
            for j in range(col):
                if arr[i][j] == 1:
                    node = (row*i)+j
                    # print(node, "-----------")
                    if disjoint_set.ultimate_parent(node) == node:
                        components += 1
        
        return n-components






n = 6
l = [[0, 0] ,[ 0,1], [1 ,0] ,[1, 2] ,[2, 1] ,[2, 2]]
print(Solution().maxRemove(l,n))



# 10
# 33 41
# 12 38
# 7 45
# 7 19
# 28 30
# 7 24
# 2 34
# 7 9
# 4 9
# 2 8