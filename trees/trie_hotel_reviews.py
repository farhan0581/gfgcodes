class Node:
    def __init__(self):
        self.children = [None]*26
        self.end = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, key):
        node = self.root
        
        for char in key:
            index = ord(char)-ord("a")

            if not node.children[index]:
                node.children[index] = Node()
            node = node.children[index]
        node.end = True


    def search(self, key):
        node = self.root

        for char in key:
            index = ord(char)-ord("a")
            
            if not node.children[index]:
                return -1
            node = node.children[index]
        return node and node.end


class Solution:
    # @param A : string
    # @param B : list of strings
    # @return a list of integers
    def solve(self, review, arr):
        t = Trie()
        for item in review.split("_"):
            t.insert(item)
        
        result = []

        for elem in arr:
            count = 0
            for item in elem.split('_'):
                r = t.search(item)
                if r == 1:
                    count += 1
            result.append(count)
        
        return [b[0] for b in sorted(enumerate(result),key=lambda i:i[1], reverse=True)]


print(Solution().solve("cool_ice_wifi_cold", ["water_is_cool", "cold_ice_drink", "cool_wifi_speed"]))