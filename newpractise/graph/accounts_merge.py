'''
Given a list of accounts where each element accounts [ i ] is a list of strings, where the first element account [ i ][ 0 ]  is a name, and the rest of the elements are emails representing emails of the account.
Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.
After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order.

Note: Accounts themselves can be returned in any order.
 

Example 1:

Input:
N = 4
accounts [ ] =
[["John","johnsmith@mail.com","john_newyork@mail.com"],
["John","johnsmith@mail.com","john00@mail.com"],
["Mary","mary@mail.com"],
["John","johnnybravo@mail.com"]]
Output:
[["John","john00@mail.com","john_newyork@mail.com", "johnsmith@mail.com"],
["Mary","mary@mail.com"],
["John","johnnybravo@mail.com"]]
Explanation:
The first and second John's are the same person as
they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none
of their email addresses are used by other accounts.
We could return these arrays in any order, for example,
the answer [['Mary', 'mary@mail.com'],
['John', 'johnnybravo@mail.com'],
['John', 'john00@mail.com', 'john_newyork@mail.com',
'johnsmith@mail.com']]
would still be accepted.
 

Example 2:

Input:
N = 5
accounts [ ] =
[["Gabe","Gabe00@m.co","Gabe3@m.co","Gabe1@m.co"],
["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],
["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],
["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],
["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
Output:
[["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],
["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],
["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],
["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],
["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
Explanation:
We don't have any common emails in any of the users.
We just sorted the emails of each person and we return a array of emails.(The details can be returned in any order).


APPROACH:
- consider every entry in the given accounts array as a node.
- Create a map of node vs email, any overlap , then do a union by size (to create the parent array)
- then again iterate
    if parent is same, good
    otherwise append in the ultimate parent


-----
Approach: 
Note: 

Here we will perform the disjoint set operations on the indices of the accounts considering them as the nodes. 
As in each account, the first element is the name, we will start iterating from the second element in each account to visit only the emails sequentially.
The algorithm steps are the following:

First, we will create a map data structure. Then we will store each email with the respective index of the account(the email belongs to) in that map data structure.
While doing so, if we encounter an email again(i.e. If any index is previously assigned for the email), we will perform union(either unionBySize() or unionByRank()) of the current index and the previously assigned index.
After completing step 2, now it’s time to merge the accounts. For merging, we will iterate over all the emails individually and find the ultimate parent(using the findUPar() method) of the assigned index of every email. Then we will add the email of the current account to the index(account index) that is the ultimate parent. Thus the accounts will be merged.
Finally, we will sort the emails for every account separately and store the final results in the answer array accordingly.

/Users/farhankhan/Desktop/gfgcodes/data/accounts_merge.png


'''
class DisJoint:
    def __init__(self, V):
        self.vertices = V
        self.parent = [i for i in range(V+1)]
        self.size = [1 for i in range(V+1)]
        self.rank = [1 for i in range(V+1)]
    
    # ultimate parent
    def ultimate_parent(self, node):
        if node == self.parent[node]:
            return node
        # call recursively and store it
        # this is called path compression 
        self.parent[node] = self.ultimate_parent(self.parent[node])
        return self.parent[node]
        
    # union by size
    def union_by_size(self, u, v):
        ultimate_parent_u = self.ultimate_parent(u)
        ultimate_parent_v = self.ultimate_parent(v)
        if ultimate_parent_u == ultimate_parent_v:
            return
        
        if self.size[ultimate_parent_u] < self.size[ultimate_parent_v]:
            self.parent[ultimate_parent_u] = ultimate_parent_v
            self.size[ultimate_parent_v] += self.size[ultimate_parent_u]
        else:
            self.parent[ultimate_parent_v] = ultimate_parent_u
            self.size[ultimate_parent_u] += self.size[ultimate_parent_v]

class Solution:
    def accountsMerge(self, accounts):
        # Code here
        n = len(accounts)
        disjoint_set = DisJoint(n-1)

        node_email = {}

        for i in range(n):
            for ind,email in enumerate(accounts[i][1:]):
                try:
                    u = node_email[email]
                    if u != i:
                        disjoint_set.union_by_size(u,i)
                    # del accounts[i][ind+1]
                except:
                    node_email[email] = i
        
        # print(disjoint_set.parent, accounts)
        merged_accounts = []
        for i in range(n):
            
            parent = disjoint_set.ultimate_parent(i)
            # print(i,parent)
            if i != parent:
                temp = accounts[i]
                accounts[parent].extend(temp[1:])
                # instead of delete, mark as empty to check later.
                accounts[i] = []
                
                # main_account = accounts[parent]
                # main_account.extend(accounts[i])
                # merged_accounts[parent] = main_account

# NOTE: never delete the entry, this will cause issue
                # del accounts[i]
            # else:
            #     merged_accounts.append(accounts[i])
            #     print(merged_accounts, "--")
        

        merged_accounts = []
        for i in range(n):
            if len(accounts[i]) == 0:
                continue
            tmp = accounts[i]
            stmp = sorted(set(tmp[1:]))
            merged_accounts.append(tmp[:1] + stmp)
        
        return merged_accounts
        # print(disjoint_set.parent, accounts)

        


N = 4
accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],
            ["John","johnsmith@mail.com","john00@mail.com"],
            ["Mary","mary@mail.com"],
            ["John","johnnybravo@mail.com"],
            ["aree", "ar@mail.com"],
            ["aree", "ar@mail.com", "pq@mail.com"]
        ]
accounts = [["mark", "mark2@gmail.com"],
            ["alice", "alice2@mail.com", "alice9@google.in", "alice6gfg.org"],
            ["fern", "fern9gfg.org", "fern3@mail","fern3@mail","fern7gfg.org", "fern2gfg.org", "fern8@mail.com"],
            ["kevin", "kevin0gfg.org", "kevin3@mail","kevin2@gmail","kevin8@gmail","kevin8@mail.com"],
            ["kevin", "kevin1@gmail","kevin6@google","kevin6@google","kevin2@mail","kevin7@google","kevin5@gmail",
            "kevin9gfg.org"],
            ["bob", "bob3@gmail","bob4@mail.com"]]
accounts = [["fern","fern1@gmail.com","fern7@mail.com","fern9@google.in","fern4@google.in","fern1@mail.com","fern1@google.in"],
            ["bob","bob8@gmail.com","bob4gfg.org"],
            ["mark","mark6@gmail.com","mark4@mail.com","mark5@mail.com","mark3@gmail.com","mark6@gmail.com"],
            ["john","john1@mail.com","john0gfg.org","john8@google.in","john2@gmail.com","john1gfg.org","john7gfg.org"],
            ["alice","alice2@google.in","alice6gfg.org","alice2@google.in","alice0@gmail.com","alice0gfg.org"],
            ["bob","bob7gfg.org","bob6@google.in","bob7@google.in","bob7@gmail.com","bob5@google.in","bob7@gmail.com","bob0gfg.org","bob7@gmail.com","bob9@mail.com"],
            ["levin","levin0gfg.org","levin2@mail.com","levin3@gmail.com","levin4gfg.org","levin1@gmail.com","levin5gfg.org","levin9@mail.com"],
            ["john","john3@gmail.com"],
            ["john","john0gfg.org","john3@mail.com","john3@mail.com"],
            ["john","john5@gmail.com","john9gfg.org","john6@gmail.com","john2@mail.com","john2@gmail.com","john7gfg.org","john9@mail.com"]]
accounts = [["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]
print(Solution().accountsMerge(accounts))




# [['fern', 'fern1@gmail.com', 'fern1@google.in', 'fern1@mail.com', 'fern4@google.in', 'fern7@mail.com', 'fern9@google.in'], ['bob', 'bob4gfg.org', 'bob8@gmail.com'], ['mark', 'mark3@gmail.com', 'mark4@mail.com', 'mark5@mail.com', 'mark6@gmail.com'], ['john', 'john0gfg.org', 'john1@mail.com', 'john1gfg.org', 'john2@gmail.com', 'john2@mail.com', 'john3@mail.com', 'john3@mail.com', 'john5@gmail.com', 'john6@gmail.com', 'john7gfg.org', 'john7gfg.org', 'john8@google.in', 'john9gfg.org'], ['alice', 'alice0@gmail.com', 'alice0gfg.org', 'alice2@google.in', 'alice6gfg.org'], ['bob', 'bob0gfg.org', 'bob5@google.in', 'bob6@google.in', 'bob7@gmail.com', 'bob7@gmail.com', 'bob7@google.in', 'bob7gfg.org'], ['levin', 'levin0gfg.org', 'levin1@gmail.com', 'levin2@mail.com', 'levin3@gmail.com', 'levin4gfg.org', 'levin5gfg.org', 'levin9@mail.com'], ['john', 'john3@gmail.com']]


# [['fern', 'fern1@gmail.com', 'fern1@google.in', 'fern1@mail.com', 'fern4@google.in', 'fern7@mail.com', 'fern9@google.in'], ['bob', 'bob4gfg.org', 'bob8@gmail.com'], ['mark', 'mark3@gmail.com', 'mark4@mail.com', 'mark5@mail.com', 'mark6@gmail.com'], ['john', 'john0gfg.org', 'john1@mail.com', 'john1gfg.org', 'john2@gmail.com', 'john2@mail.com', 'john3@mail.com', 'john5@gmail.com', 'john6@gmail.com', 'john7gfg.org', 'john8@google.in', 'john9@mail.com', 'john9gfg.org'], ['alice', 'alice0@gmail.com', 'alice0gfg.org', 'alice2@google.in', 'alice6gfg.org'], ['bob', 'bob0gfg.org', 'bob5@google.in', 'bob6@google.in', 'bob7@gmail.com', 'bob7@google.in', 'bob7gfg.org', 'bob9@mail.com'], ['levin', 'levin0gfg.org', 'levin1@gmail.com', 'levin2@mail.com', 'levin3@gmail.com', 'levin4gfg.org', 'levin5gfg.org', 'levin9@mail.com'], ['john', 'john3@gmail.com']]