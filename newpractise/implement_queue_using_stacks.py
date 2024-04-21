'''
we use 2 stacks
s1 and s2
on insert
- pop everyting from s1 and put to s2
- insert new item in s1
- pop everyting from s2 and put back to s1

'''
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

        

    def push(self, x: int) -> None:
        
        while self.stack1:
            item = self.stack1.pop()
            self.stack2.append(item)
        
        self.stack1.append(x)

        while self.stack2:
            item = self.stack2.pop()
            self.stack1.append(item)
        
        return


        

    def pop(self) -> int:
        return self.stack1.pop()
        

    def peek(self) -> int:
        return self.stack1[-1]
        

    def empty(self) -> bool:
        return len(self.stack1) == 0