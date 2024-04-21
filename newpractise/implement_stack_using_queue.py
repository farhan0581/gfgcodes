from queue import Queue

class MyStack:

    def __init__(self):
        self.queue = Queue()
        self.front = 0
        self.rear = 0
        

    def push(self, x: int) -> None:
        self.queue.put(x)

        for i in range(0, self.queue.qsize-1):
            self.queue.put(self.queue.get())

    def pop(self) -> int:
        elem = self.queue.get()
        return elem

    def top(self) -> int:
        return self.queue.queue[0]
        

    def empty(self) -> bool:
        return len(self.queue) == 0