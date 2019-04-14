class Node:
    def __init__(self):
        self.children = [[None,0]]*26
        self.end = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, key):
        node = self.root
        
        for char in key:
            index = ord(char)-ord("a")
            if not node.children[index][0]:
                node.children[index] = [Node(), 1]
            else:
                node.children[index][1] += 1
            node = node.children[index][0]
        node.end = True


    def search(self, key):
        node = self.root

        for char in key:
            index = ord(char)-ord("a")
            
            if not node.children[index][0]:
                return -1
            node = node.children[index][0]
        return 1
    
    def min_prefix(self, key):
        # print(key)
        node = self.root
        prefix = ''
        # f = True

        for char in key:
            index = ord(char)-ord("a")
            node = node.children[index]
            if node[1] > 1:
                # print(char)
                prefix += char
                # f = False
            if node[1] == 1:
                prefix += char
                break
            node = node[0]
        # prefix += char

        return prefix


class Solution:
    # @param A : list of strings
    # @return a list of strings
    def prefix(self, arr):
        result = []
        t = Trie()
        for item in arr:
            t.insert(item)
            # print(t.root.children)
        
        for item in arr:
            result.append(t.min_prefix(item))
        
        return result

# obj = Trie()
# obj.insert('sd')
# print(obj.search('sd'))

print(Solution().prefix(['zebra', 'dog', 'duck', 'dove', 'far', 'khan', 'khanna']))
