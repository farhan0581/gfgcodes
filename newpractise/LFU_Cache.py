class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None
        self.freq = 1

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def delete(self):
        if not self.tail:
            return
        temp = self.tail
        self.tail = self.tail.prev
        
        if temp.prev:
            temp.prev.next = None
        
        if self.head == temp:
            self.head = None
        
        self.size -= 1
        return temp
    
    def insert(self, node):

        if self.head:
            self.head.prev = node
            node.next = self.head
        
        self.head = node

        if not self.tail:
            self.tail = node
        
        self.size += 1
    
    def remove_node(self, node):
        
        prevNode = node.prev
        nextNode = node.next

        if prevNode:
            prevNode.next = nextNode
        if nextNode:
            nextNode.prev = prevNode
        
        if node == self.tail:
            self.tail = prevNode
        
        if node == self.head:
            self.head = nextNode
        
        self.size -= 1


class LFUCache:

    def __init__(self, capacity: int):
        self.maxCap = capacity
        self.cap = 0
        self.minFreq = 0
        self.map_ll = {}
        self.map = {}
    
    def _update(self, node):
        freq = node.freq
        # print(self.map_ll)
        # print(self.map)
        old_ll = self.map_ll[freq]
        old_ll.remove_node(node)

        if self.minFreq == freq and not old_ll.size:
            self.minFreq = freq + 1

        freq += 1


        ll = self.map_ll.get(freq, None)
        if not ll:
            ll = DoublyLinkedList()
        
        ll.insert(node)
        self.map_ll[freq] = ll
        node.freq = freq


    def get(self, key: int) -> int:
        node = self.map.get(key, None)
        if not node:
            print(-1)
            return -1
        
        self._update(node)
        print(node.val)
        return node.val
    
    def delete(self):
        # print(self.map_ll[self.minFreq])
        ll = self.map_ll[self.minFreq]
        node = ll.delete()
        
        print("========", self.minFreq)
        # if node:
        print(node.val)
        key = node.key
        del self.map[key]
        self.cap -= 1
        # else:
        #     print("unable to delete")
    
    def insert(self, key, val):
        node = Node(key, val)
        self.minFreq = 1

        ll = self.map_ll.get(1, None)
        if not ll:
            ll = DoublyLinkedList()
        
        ll.insert(node)
        self.map_ll[1] = ll
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
            self._update(node)
    
    def print_list(self):
        for k,ll in self.map_ll.items():

            cur = ll.head
            l = []
            while cur:
                l.append(str(cur.val))
                cur = cur.next
            
            head = ll.head.val if ll.head else "None"
            tail = ll.tail.val if ll.tail else "None"
            print("F: %d, Head:%s , Tail:%s , List:%s " % (k, head, tail, "->".join(l)))
        print("------------------------------------")


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


        
        

lfu = LFUCache(2)
lfu.put(1, 1)   # cache=[1,_], cnt(1)=1
lfu.put(2, 2)   # cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.print_list()
lfu.get(1)      # return 1
                 # cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.print_list()
lfu.put(3, 3)   # 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 # cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.print_list()
lfu.get(2)      # return -1 (not found)
lfu.get(3)      # return 3
                 # cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.print_list()
lfu.put(4, 4)   # Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 # cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.print_list()
lfu.get(1)      # return -1 (not found)
lfu.get(3)      # return 3
                 # cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.print_list()
lfu.get(4)      # return 4
                 # cache=[4,3], cnt(4)=2, cnt(3)=3