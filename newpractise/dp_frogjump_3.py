'''
You are given a 0-indexed integer array stones sorted in strictly increasing order representing the positions of stones in a river.

A frog, initially on the first stone, wants to travel to the last stone and then return to the first stone. However, it can jump to any stone at most once.

The length of a jump is the absolute difference between the position of the stone the frog is currently on and the position of the stone to which the frog jumps.

More formally, if the frog is at stones[i] and is jumping to stones[j], the length of the jump is |stones[i] - stones[j]|.
The cost of a path is the maximum length of a jump among all jumps in the path.

Return the minimum cost of a path for the frog.


Approach
No matter how you try, the best approach is always going to be skipping the next stone and going to next stone after that (if this step is possible).

After drawing all possibilities it can be seen that the biggest steps are always going to be skipping one stone in between of two stones, i.e of length = 2.
There may be other steps as well of length = 1 but there will always be another step of length 2 skipping over the stone involved in jump of length 1, hence making the length 1 jump not worth considering.

Here are examples of possible paths for even and odd number of stones.
Sorry for unclear photos.

odd1.jpg

even1.jpg

As, the images can hopefully show, the optimal path will result in jumps of length 2, and so in the code I have just used two pointers i, j to iterate through the graph and check what is the maximum cost in jumping this way.

Hope you understood what I am trying to convey here. Anyways, have a great day and Happy Coding.

'''
# kul mila ke saare draw kar ke dekh lo, best possible is to have alternate jumps
# us mein bhi bas hamein 2 length walon ko check karna for the max

class Solution(object):
    def maxJump(self, stones):
        if len(stones) == 2:
            return stones[1]-stones[0]
        
        i = 0
        j = 2
        maxjump = 0
        while j < len(stones):
            maxjump = max(maxjump, stones[j]-stones[i])
            i += 1
            j += 1
        
        return maxjump

        
l=[0,2,7]
print(Solution().maxJump(l))