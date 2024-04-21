'''
Two players play a turn based game on a binary tree. We are given the root of this binary tree, and the number of nodes n in the tree. n is odd, and each node has a distinct value from 1 to n.

Initially, the first player names a value x with 1 <= x <= n, and the second player names a value y with 1 <= y <= n and y != x. The first player colors the node with value x red, and the second player colors the node with value y blue.

Then, the players take turns starting with the first player. In each turn, that player chooses a node of their color (red if player 1, blue if player 2) and colors an uncolored neighbor of the chosen node (either the left child, right child, or parent of the chosen node.)

If (and only if) a player cannot choose such a node in this way, they must pass their turn. If both players pass their turn, the game ends, and the winner is the player that colored more nodes.

You are the second player. If it is possible to choose such a y to ensure you win the game, return true. If it is not possible, return false.
https://assets.leetcode.com/uploads/2019/08/01/1480-binary-tree-coloring-game.png


APPROACH:
- the only condition to win for second player is that, it can color the left, right or parent of
the node which was colored in first step by player one.
only if the count of nodes in (left, right, parent) > half of tree nodes

'''

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, node, lc, rc, x):
        if not node:
            return 0, lc, rc, x
        
        leftCount, lc, rc, x = self.countNodes(node.left, lc, rc, x)
        rightCount, lc, rc, x = self.countNodes(node.right, lc, rc, x)
        
        if node.val == x:
            lc = leftCount
            rc = rightCount

        return leftCount + rightCount + 1, lc, rc, x
        

    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        t, lc, rc, x = self.countNodes(root, 0, 0, x)
        
        maxChild = max(lc, rc)
        parentCount = n - lc - rc - 1 

        if max(maxChild, parentCount) > n//2:
            return True
        return False 