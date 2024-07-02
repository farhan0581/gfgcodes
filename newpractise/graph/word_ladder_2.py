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


upar wali approach tab kaam karegi jab hamein sequence nahein chayein, seq ke liye alag hai thoda logic:
- hamein queueu mein poora sequence store karna hoga,
- jab bhi q se pop karne ke baad seq ki length cur level se zyada ho jaaye to , map se delete karo
- neeche map se delete ni karna hai, becoz , same word, 2 alag alag sequence ka part ho sakta hai, is liye
  use use hone do
- seq ki length hi hamein level batayegi , becoz ye bfs hai ? kaise ?
  q = [[1]] level 1
  q = [[1,2]] level 2
  q = [[1,2],[1,2,3]] level 2 hi rahega, front se le rahe hain, to jab tak ek level ke saare
      pure nahein ho jaate, hamara length nahein badegi, jaise hi pehla element mila jis ki
      length zyada hai, is ka matlab last level is complete
      phir ham last level mein jo words use huey hain unhe delete kar sakte hain



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
        m[beginWord] = True

        res = []
        # this is a list of sequence now
        q = [[beginWord]]
        curlevel = 0
        used_on_level = [beginWord]

        while len(q) > 0:
            w = q.pop(0)
            word = w[-1] # last word is the new word
            
            # matlab last level is over
            if curlevel < len(w):
                for rw in used_on_level:
                    if m.get(rw, False):
                        del m[rw]
                curlevel += 1
                used_on_level = []
                

            if word == endWord:
                # first occurance if result is shortest
                if len(res) == 0:
                    res.append(w)
                else:
                    # check if its not longer than first result (shortest)
                    if len(res[0]) == len(w):
                        res.append(w)


            for i in range(len(word)):
                for j in string.ascii_lowercase:
                    newWord = word[:i] + j + word[i+1:]
                    if m.get(newWord) and newWord != word:
                        w.append(newWord)
                        q.append(w[:])
                        # word replace karna hai , otherwsie follow string cat approach
                        w.pop(-1)
                        used_on_level.append(newWord)
        
            
        return res


beginWord = "der"
endWord = "dfs"
wordList = ["des","der","dfr","dgt","dfs"]
# wordList = ["hot","dot","dog","lot","log","cog"]

print(Solution().ladderLength(beginWord, endWord, wordList))