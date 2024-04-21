
class MinHeap:
    def __init__(self, maxsize) -> None:
        self.front = 0
        self.size = 0
        self.maxsize = maxsize
        self.heap = [-1]*maxsize

    
    def left_child(self, index):
        return 2*index+1

    def right_child(self, index):
        return 2*index+2

    def parent(self, index):
        return index // 2

    def is_leaf(self, index):
        if 2*index+1 > self.size:
            return True
        return False

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def get_min(self):
        print(self.heap)
        return self.heap[self.front]
    
    def heapify(self, index):
        
        if not self.is_leaf(index):
            
            if self.heap[index] > self.heap[self.left_child(index)] or self.heap[index] > self.heap[self.right_child(index)]:
                
                if self.heap[self.left_child(index)] < self.heap[self.right_child(index)]:
                    self.swap(index, self.left_child(index))
                    self.heapify(self.left_child(index))
                else:
                    self.swap(index, self.right_child(index))
                    self.heapify(self.right_child(index))
    

    def insert(self, value):
        if self.size >= self.maxsize:
            self.delete()
        
        self.heap[self.size] = value
        cur = self.size
        self.size += 1

        while self.heap[cur] < self.heap[self.parent(cur)]:
            self.swap(cur, self.parent(cur))
            cur = self.parent(cur)


    def delete(self):
        val = self.heap[self.front]
        print("deleting value =", val)
        self.heap[self.front] = self.heap[self.size-1] 
        self.size -= 1
        self.heapify(self.front)

    

hp = MinHeap(5)

li = [5,31,3,7,2,19,1]

for item in li:
    hp.insert(item)
    print(hp.get_min())

print(hp.get_min())
