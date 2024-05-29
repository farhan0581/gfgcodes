'''
Given a sorted dictionary of an alien language having N words and k starting alphabets of standard dictionary. Find the order of characters in the alien language.
Note: Many orders may be possible for a particular test case, thus you may return any valid order and output will be 1 if the order of string returned by the function is correct else 0 denoting incorrect string returned.
 

Example 1:

Input: 
N = 5, K = 4
dict = {"baa","abcd","abca","cab","cad"}
Output:
1
Explanation:
Here order of characters is 
'b', 'd', 'a', 'c' Note that words are sorted 
and in the given language "baa" comes before 
"abcd", therefore 'b' is before 'a' in output.
Similarly we can find other orders.
Example 2:

Input: 
N = 3, K = 3
dict = {"caa","aaa","aab"}
Output:
1
Explanation:
Here order of characters is
'c', 'a', 'b' Note that words are sorted
and in the given language "caa" comes before
"aaa", therefore 'c' is before 'a' in output.
Similarly we can find other orders.
 

Your Task:
You don't need to read or print anything. Your task is to complete the function findOrder() which takes  the string array dict[], its size N and the integer K as input parameter and returns a string denoting the order of characters in the alien language.


Expected Time Complexity: O(N * |S| + K) , where |S| denotes maximum length.
Expected Space Compelxity: O(K)
'''
#User function Template for python3

class Solution:
    def findEdge(self, w1, w2):
        i = j = 0
        while i < len(w1) and j < len(w2):
            if w1[i] != w2[j]:
                return [ord(w1[i])-97, ord(w2[j])-97]
            i += 1
            j += 1
        return []
        
    def findOrder(self,alien_dict, N, K):
        edges = []
        
        i = 1
        while i < len(alien_dict):
            w1 = alien_dict[i-1]
            w2 = alien_dict[i]
            ed = self.findEdge(w1,w2)
            if len(ed) > 0:
                edges.append(ed)
            
            i += 1
            
        adj = [[] for i in range(K)]
        indegrees = [0 for i in range(K)]
        
        for edge in edges:
            u,v = edge
            adj[u].append(v)
            indegrees[v] += 1
        
        q = []
        for ind, val in enumerate(indegrees):
            if val == 0:
                q.append(ind)
        
        safe = []
        while len(q) > 0:
            node = q.pop(0)
            safe.append(node)
            
            for adjNode in adj[node]:
                indegrees[adjNode] -= 1
                
                if indegrees[adjNode] == 0:
                    q.append(adjNode)
        
        res = [chr(item+97) for item in safe]
        # print(res)
        return res