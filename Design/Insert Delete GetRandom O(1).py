# Key: how to choose a random index and then to retrieve an element with that index.
# map<val, list_index> + list
# before poping, swap the target val to the end of list

import random


class RandomizedSet:

    def __init__(self):
        self.map = {}  # <val, index_in_list>
        self.list = []

    # Returns true if the item was not present, false otherwise.
    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        else:
            self.list.append(val)
            self.map[val] = len(self.list) - 1
            return True

    # Swap the element to delete with the last one, then pop(); also update index in map
    # Returns true if the item was present, false otherwise.
    def remove(self, val: int) -> bool:
        if val in self.map:
            index = self.map.pop(val)

            if index == len(self.list) - 1:
                self.list.pop()
            else:  # need to swap elements in list, and update index in map for the affected element
                self.list[index], self.list[-1] = self.list[-1], self.list[index]
                self.list.pop()
                self.map[self.list[index]] = index
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.list)
        # return self.list[random.randint(0, len(self.list) - 1)] # Equivalent

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()