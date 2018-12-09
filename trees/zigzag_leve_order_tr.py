class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.val = value

def zigzagLevelOrder(node):
    queue = [node]
    result = []
    reverse = 0

    def get_res(queue, reverse):
        _q = []
        _r = []
        for node in queue:
            if node:
                _r.append(node.val)
            if node.left:
                _q.append(node.left)
            if node.right:
                _q.append(node.right)
        
        if reverse == 1:
            result.append(_r[::-1])
        else:
            result.append(_r)
        reverse = 0 if reverse == 1 else 1
        return _q, reverse
    
    while len(queue) > 0:
        queue, reverse = get_res(queue, reverse)
    
    return result
    
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)

print(zigzagLevelOrder(root))