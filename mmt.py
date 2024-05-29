'''
1 2 3 = m 

O(m) + 2*n  


3 1 2
 
2 


1 2 3 1

1 3 


1 : [0,3]
2 : 1
'''

def solve(mapPos, arr, i, prev):
    if i >= len(arr):
        return 0

    # take
    take = nottake = 0
    positions = mapPos.get(arr[i], [])
    maxBridges = 0

    for j in range(len(positions)):
        pos = positions[j]
        if prev == -1 or prev < pos:
            take = 1 + solve(mapPos, arr, i+1, pos)
        
            #not take
        nottake = solve(mapPos, arr, i+1, prev) + 0
        
        maxBridges = max(maxBridges, take, nottake)

    
    return maxBridges


def findMaxBridges(arr1, arr2):
    mapPos = {}
    
    for i in range(len(arr1)):
        tmp = mapPos.get(arr1[i], [])
        tmp.append(i)
        mapPos[arr1[i]] = tmp
    
    return solve(mapPos, arr2, 0, -1)


arr1 = []
arr2 = []

# max_bridges = findMaxBridges(arr1, arr2)
# print(max_bridges)

'''
prev = 0*10
    6
  3     5
2   5      4
   7  4

'''

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def dfs(node, prev, result):
    if not node:
        return 0 
    
    # leaf
    if node and not node.left and not node.right:
        result += prev*10 + node.val
    
    prev = prev*10 + node.val
    
    if node.left:
        result = dfs(node.left, prev, result)
    
    if node.right:
        result = dfs(node.right, prev, result)
    

    return result



def getTotalSum(root):
    return dfs(root, 0, 0)


root = TreeNode(6)
left = TreeNode(3)
right = TreeNode(5)
root.left = left
root.right = right
root.left.left = TreeNode(2)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right.right = TreeNode(4)

'''
prev = 0*10
    6
  3     5
2   5      4
   7  4

'''



# print(getTotalSum(root))

l = [[1,3],[2,6],[-8,10],[15,18]]
l = sorted(l, key=lambda x:x[0])
print(l)


'''
LLD

1. design an order system with a set of complex order configurations having room and rates for a hotel.
2. design LRU Cache
3. rest and restful apis
4. ACID and normalization
5. LLD kafka
6. Design an api which support 1 million req/sec to be stored in a datastore and order needs to be maintained.
7. program to input stream of numbers and then get the output of squares.
8. program to download content from the make my trip website and count the number of occurances.Multiple
    such webistes can be input and show parralel execution in golang
'''