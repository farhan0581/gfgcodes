'''
You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

You start on square 1 of the board. In each move, starting from square curr, do the following:

Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
The game ends when you reach the square n2.
A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n2 do not have a snake or ladder.

Note that you only take a snake or ladder at most once per move. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.

For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
Return the least number of moves required to reach the square n2. If it is not possible to reach the square, return -1.
https://assets.leetcode.com/uploads/2018/09/23/snakes.png

'''

from typing import List

class Solution:
    # this converts pos to row and column
    def convert(self, pos, n):
        pos -= 1
        r = pos // n
        remainder = pos % n
        if r % 2 == 0:
            c = remainder
        else:
            c = (n-remainder)-1     
        return n-r-1, c

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        q = [[1, 0]]
        vis = [-1]*(n*n+1)

        while len(q) > 0:
            pos, dis = q.pop(0)

            for j in range(1, min(n*n+1, 6)+1):
                newPos = pos + j
                r,c = self.convert(newPos,n)

                # if snake or ladder then we need to jump
                if board[r][c] != -1:
                    newPos = board[r][c]
                
                # check if we reached the last cell
                if newPos == n*n:
                    return dis+1

                # keep visited array to not visit again, in case of snake
                if vis[newPos] == -1:
                    vis[newPos] = 1
                    q.append([newPos, dis+1])
        
        return -1
                    




