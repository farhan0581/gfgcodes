class Node:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

def print_vertical_order(map_dist, node, dist):
    if not node:
        return
    try:
        map_dist[dist].append(node)
    except:
        map_dist[dist] = [node] 

    print_vertical_order(map_dist, node.left, dist-1)
    print_vertical_order(map_dist, node.right, dist+1)

def get_vertical_order(root):
    map_dist = {}
    print_vertical_order(map_dist, root, 0)
    
    sorted(map_dist)
    for key, value in map_dist.items():
        print('------(%s)------' % key)
        for i in value:
            print(i.val)


root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(8)
root.left.right.right.left = Node(9)
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)
get_vertical_order(root)