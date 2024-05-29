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
            return
        
        if self.size[ultimate_parent_u] < self.size[ultimate_parent_v]:
            self.parent[ultimate_parent_u] = ultimate_parent_v
            self.size[ultimate_parent_v] += self.size[ultimate_parent_u]
        else:
            self.parent[ultimate_parent_v] = ultimate_parent_u
            self.size[ultimate_parent_u] += self.size[ultimate_parent_v]

    def union_by_rank(self):
        pass
    

o = DisJoint(7)
o.union_by_size(1,2)
print(o.parent, o.size)
o.union_by_size(2,3)
print(o.parent, o.size)
o.union_by_size(4,5)
print(o.parent, o.size)
o.union_by_size(6,7)
print(o.parent, o.size)
o.union_by_size(5,6)
print(o.parent, o.size)

# print(o.ultimate_parent(3))
# print(o.ultimate_parent(7))

o.union_by_size(3,7)
print(o.parent, o.size)

# print(o.ultimate_parent(3))
# print(o.ultimate_parent(7))

# print(o.parent)

