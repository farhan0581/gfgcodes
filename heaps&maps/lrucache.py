class Node:
    def __init__(self, key=None, value=None):
        self.val = value
        self.key = key
        self.left = None
        self.right = None


class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.cur_capacity = 0
        self.map = {}
        self.start = None
        self.end = None

    def update_position(self, node):
        if self.start == node:
            return
        elif node.left and node.right:
            temp = node.left
            node.left.right = node.right
            node.right.left = temp
            node.right = self.start
            node.left = None
            self.start.left = node
            self.start = node
        elif node.left and not node.right:
            self.end = node.left
            temp = node.left
            node.left.right = None
            node.left = None
            node.right = self.start
            self.start.left = node
            self.start = node

    # @return an integer
    def get(self, key):
        node = self.map.get(key)
        if node:
            self.update_position(node)
            return node.val
        return -1
    
    def create_new_node(self, key, value):
        node = Node(key, value)
        node.right = self.start
        # first node
        if self.start == None:
            self.end = node
        try:
            self.start.left = node
        except:
            pass
        self.start = node
        self.map[key] = node
        return node

    def set(self, key, value):
        node = self.map.get(key)
        
        # already exists
        if node:
            node.val = value
            self.update_position(node)
        
        # new object
        else:
            new_node = self.create_new_node(key, value)
            if self.cur_capacity < self.capacity:
                self.cur_capacity += 1
            else:
                lastnode = self.end
                del self.map[lastnode.key]
                if lastnode:
                    if lastnode.left:
                        self.end = lastnode.left
                        lastnode.left.right = None
                    else:
                        self.end = new_node
                
    
    def iterate(self):
        cur = self.start
        vals = []
        while cur:
            vals.append(str(cur.val))
            cur = cur.right
        print('->'.join(vals))
        print('--------------')


obj = LRUCache(1)
obj.set(2, 1)
# print(obj.end.val)
obj.set(2, 2)
# print(obj.end.val)
# obj.iterate()
print(obj.get(2))
print(obj.get(1))
print(obj.get(10))
obj.set(1, 1) 
obj.set(4, 1)
# obj.iterate()
print(obj.map)
print(obj.get(2))
# obj.iterate()

# S 2 1 S 2 2 G 2 S 1 1 S 4 1 G 2