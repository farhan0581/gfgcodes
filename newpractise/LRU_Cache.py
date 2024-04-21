class DoublyLinkedList:
    def __init__(self, key, val):
        self.prev = None
        self.next = None
        self.val = val
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.maxCap = capacity
        self.cap = 0
        self.ll = None
        self.head = None
        self.tail = None
        self.map = {}
    
    def change_node_pos(self, node):
        if self.head == node:
            return

        if self.tail == node:
            self.tail = node.prev
        
        prevNode = node.prev
        nextNode = node.next

        if prevNode:
            prevNode.next = nextNode
        if nextNode:
            nextNode.prev = prevNode
        
        if self.head:
            self.head.prev = node
            node.next = self.head
            self.head = node


    def get(self, key: int) -> int:
        node = self.map.get(key, None)
        if not node:
            return -1
        
        self.change_node_pos(node)
        return node.val
    
    def delete(self):
        if not self.tail:
            return
        
        temp = self.tail
        self.tail = self.tail.prev
        if temp.prev:
            temp.prev.next = None
        
        key = temp.key
        del self.map[key]
        self.cap -= 1
    
    def insert(self, key, val):
        node = DoublyLinkedList(key, val)

        if self.head:
            self.head.prev = node
            node.next = self.head
        self.head = node

        if not self.tail:
            self.tail = node
        
        self.map[key] = node
        self.cap += 1

    def put(self, key: int, value: int) -> None:
        node = self.map.get(key, None)
        if not node:
            if self.cap >= self.maxCap:
                self.delete()
            self.insert(key, value)
        else:
            node.val = value
            self.change_node_pos(node)
    
    def print_list(self):
        cur = self.head
        l = []
        while cur:
            l.append(str(cur.val))
            cur = cur.next
        
        print("Head:%s , Tail:%s , List:%s " % (self.head.val, self.tail.val, "->".join(l)))


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


        
        

lRUCache = LRUCache(2)
lRUCache.put(1, 1) # cache is {1=1}
lRUCache.put(2, 2) # cache is {1=1, 2=2}
lRUCache.print_list()
lRUCache.get(1)    # return 1
lRUCache.print_list()
lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.print_list()
lRUCache.get(2)    # returns -1 (not found)
# lRUCache.print_list()
lRUCache.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1)    # return -1 (not found)
lRUCache.get(3)    # return 3
lRUCache.get(4)    # return 4