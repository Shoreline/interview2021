# Hashmap + double linkedlist
# Use a map of <key, node> to access nodes in O(1) time
# Access sequence is obtained by maintaining a double linked list that always keeps nodes in the order of operate (put/get) time.
# Build a refresh_head(key) function and call it everytime finish accessing a node.
# refresh_head(key) is also responsible for dropping tail node if bypassing capacity.

# A class for double linkedlist node
class Node:
    def __init__(self, key: int, value: int, pre: 'Node' = None, next: 'Node' = None):
        self.key = key
        self.val = value
        self.pre = None
        self.next = None


# a map (cache) to save actual items; a double linkedlist to save access sequence
class LRUCache():
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # <int, node> map
        self.head = None
        self.tail = None

    # if key exist in cache: 1) move the node of key to head and 2) return value.
    # if not exist return -1.
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.refresh_head(key)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value  # update the value for the given key
        else:
            new_node = Node(key, value)
            self.cache[key] = new_node
            if not self.head:  # if this new node is the only node in cache
                self.head = new_node
                self.tail = new_node
            else:
                self.head.pre = new_node
                new_node.next = self.head
                self.head = new_node
        self.refresh_head(key)

        # refresh_head is also responsible for dropping tail node if bypassing capacity

    def refresh_head(self, key: int):
        node = self.cache[key]

        if self.head != node:
            # 1) cut this node out
            if self.tail == node:
                self.tail = node.pre
                self.tail.next = None
            else:
                node.pre.next = node.next
                node.next.pre = node.pre

            # 2) set this node to be the new head
            self.head.pre = node
            node.next = self.head
            node.pre = None
            self.head = node

        if len(self.cache) > self.capacity:
            self.cache.pop(self.tail.key)
            self.tail = self.tail.pre
            self.tail.next = None

# # OrderedDict combines hashmap and linkedlist (in Java it's LinkedHashMap)
# from collections import OrderedDict
# class LRUCache(OrderedDict): # inheritance in python: parent class is OrderedDict

#     def __init__(self, capacity: int):
#         self.capacity = capacity

#     def get(self, key: int) -> int:
#         if key not in self:
#             return -1
#         self.move_to_end(key)
#         return self[key]

#     def put(self, key: int, value: int) -> None:
#         if key in self:
#             self.move_to_end(key)
#         self[key] = value
#         if len(self) > self.capacity:
#             self.popitem(last = False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)