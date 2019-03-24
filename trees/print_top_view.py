# done using level order traversal(using queue)
# and used strategy(map) of vertical order traversal

class Node:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

def print_top_view(q, map_dist):
    
    while q:
        val = q[0]
        del q[0]
        # front += 1
        if val[0].left:
            q.append((val[0].left, val[1] - 1))
        if val[0].right:
            q.append((val[0].right, val[1]+1))

        if val[1] not in map_dist:
            map_dist[val[1]] = val[0]

def get_top_view(root):
    map_dist = {}
    queue = [(root,0)]
    print_top_view(queue, map_dist)
    
    sorted(map_dist)
    for key, value in map_dist.items():
        print('------(%s)------' % key)
        print(value.val)


# root = Node(1)
# root.left = Node(2)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.left.right.right = Node(8)
# root.left.right.right.left = Node(9)
# root.right = Node(3)
# root.right.left = Node(6)
# root.right.right = Node(7)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.right.right = Node(5)
root.left.right.right.right = Node(6)
get_top_view(root)