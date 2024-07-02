'''
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

APPROACH:
1. for all the possible positions of a word we will generate all the words possible
2. Then for each generated word will be pushed to queue for bfs
3. why bfs ?
because if we look, this is a level order traversal , because each level increase by 1
hamein last level hi return karna hai
visited array hamari map ban gayi hai, ek baar word visit kara to use dobara visit nahein karna hai
is approach mein sequence nahein pata chalega

/Users/farhankhan/Desktop/gfgcodes/data/word_tr1.png
'''
import string    

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
        m = {word:True for word in wordList}

        # res = []
        q = [(beginWord, 1)]

        while len(q) > 0:
            w, seq = q.pop(0)
            # res.append(w)
            if w == endWord:
                return seq

            for i in range(len(w)):
                for j in string.ascii_lowercase:
                    newWord = w[:i] + j + w[i+1:]
                    if m.get(newWord) and newWord != w:
                        q.append((newWord, seq+1))
                        del m[newWord]
        return 0


beginWord = "der"
endWord = "dfs"
wordList = ["des","der","dfr","dgt","dfs"]
# wordList = ["hot","dot","dog","lot","log","cog"]

print(Solution().ladderLength(beginWord, endWord, wordList))