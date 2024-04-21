'''
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

 

Example 1:

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.

'''

import random
class RandomizedSet:

    def __init__(self):
        self.map = dict()
        self.list = list()
        

    def insert(self, val: int) -> bool:
        # print("insert: ", val, self.map, self.list)
        ind = self.map.get(val, -1)
        if ind == -1:
            self.list.append(val)
            ind = len(self.list) - 1
            self.map[val] = ind
            # print("insert: ", val, self.map, self.list)
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        # print("remove: ", val, self.map, self.list)
        ind = self.map.get(val, -1)
        if ind > -1:
            lastInd = len(self.list)-1
            lastVal = self.list[lastInd]
            self.list[lastInd], self.list[ind] = self.list[ind], self.list[lastInd]
            self.list.pop()
            self.map[lastVal] = ind
            del self.map[val]
            # print("remove: ", val, self.map, self.list)
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        # print(self.list)
        return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()