class MinStack(object):
    def __init__(self, *args, **kwargs):
        super(MinStack, self).__init__(*args, **kwargs)
        self.aux_stack = []
        self.stack = []

    def push(self, x):
        self.stack.append(x)
        if self.aux_stack:
            if self.aux_stack[-1] > x:
                self.aux_stack.append(x)
            else:
                self.aux_stack.append(self.aux_stack[-1])
        else:
            self.aux_stack.append(x)
    # @return nothing
    def pop(self):
        if self.stack:
            del self.stack[-1]
            del self.aux_stack[-1]

    # @return an integer
    def top(self):
        if not self.stack:
            return -1
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        if not self.stack:
            return -1
        return self.aux_stack[-1]


stack = MinStack()
print(stack.getMin())
print(stack.top())
stack.push(18)
stack.push(19)
stack.push(29)
stack.push(15)
stack.push(16)
print(stack.getMin())
stack.pop()
stack.pop()
print(stack.getMin())