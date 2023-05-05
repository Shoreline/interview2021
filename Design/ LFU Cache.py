from collections import defaultdict
from collections import OrderedDict

class Node:
    def __init__(self, key, val, count):
        self.key = key
        self.val = val
        self.count = count


class LFUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.key2node = {}
        # When there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be
        # invalidated. -> Use OrderedDict for simplicity.
        self.count2nodes = defaultdict(OrderedDict) # a map of ordered map: <count,OrderedDict<key,node>>
        self.minCount = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key2node:
            return -1

        node = self.key2node[key]
        del self.count2nodes[node.count][key]

        # clean up empty counts
        if not self.count2nodes[node.count]:
            del self.count2nodes[node.count]

        node.count += 1
        self.count2nodes[node.count][key] = node

        # NOTICE check minCount!!!
        if not self.count2nodes[self.minCount]:
            self.minCount += 1

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
            k, n = self.count2nodes[self.minCount].popitem(last=False) # By default last=True
            del self.key2node[k]

        self.count2nodes[1][key] = self.key2node[key] = Node(key, value, 1)
        self.minCount = 1
        return

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)