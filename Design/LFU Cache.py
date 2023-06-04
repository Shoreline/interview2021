# Two maps
# <key, (val, count)>
# <count, OrderedDict<key, (val, count)>>
# If don't use OrderedDict, we can also use doubly linked list (add self.pre and self.next to Node class)

from collections import defaultdict
from collections import OrderedDict


class Node:
    def __init__(self, key, val, count):
        self.val = val
        self.count = count


class LFUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.key2node = {}
        self.count2node = defaultdict(OrderedDict)
        self.minCount = None  # tracks the least frequency count at the moment

    # Also called in put() to update frequency count for a key
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key2node:
            return -1

        node = self.key2node[key]

        # clean memory (optional)
        # if not self.count2node[node.count]:
        #     del self.count2node[node.count]

        # Update minCount if this node is the only node having minCount
        if node.count == self.minCount and len(self.count2node[node.count]) == 1:
            self.minCount += 1

        # To update count2node map (map of map), we have to remove the existing item first
        del self.count2node[node.count][key]
        node.count += 1
        self.count2node[node.count][key] = node

        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if not self.cap:
            return

        if key in self.key2node:
            self.key2node[key].val = value
            self.get(key)  # NOTICE, put makes count+1 too
            return

        if len(self.key2node) == self.cap:
            # popitem(last=False) is FIFO, like queue
            # it return key and value!!!
            k, n = self.count2node[self.minCount].popitem(last=False)
            del self.key2node[k]

        self.count2node[1][key] = self.key2node[key] = Node(key, value, 1)
        self.minCount = 1  # new iteam, so new least frequency count is 1.
        return

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)