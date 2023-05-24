# copied from official solution

# The TrieNode data structure.

# Time Complexity:
#  create ~ It takes O(n) to add a path to the trie if it contains n components.
#  get ~ It takes O(n) to find a path in the trie if it contains n components.
#
# Space Complexity:
#  create ~ Lets look at the worst case space complexity. In the worst case, none of the paths will have any common
# prefixes. We are not considering the ancestors of a larger path here. In such a case, each unique path will end up
# taking a different branch in the trie. Also, for a path containing n components, there will be n nodes in the
# trie.
#  get ~ O(1).

# class TrieNode(object):
class TrieNode:
    def __init__(self, name):
        self.map = defaultdict(TrieNode)
        self.name = name
        # we are told a created path has an associated value. (note there won't be any "middle node" by the rule
        self.value = -1


class FileSystem:

    def __init__(self):
        # Root node contains the empty string.
        self.root = TrieNode("")

    # Creates a new path and associates a value to it if possible and returns true. Returns false if the path already
    # exists or its parent path doesn't exist.
    def createPath(self, path: str, value: int) -> bool:

        # Obtain all the components
        components = path.split("/")

        # Start "curr" from the root node.
        cur = self.root

        # Iterate over all the components.
        for i in range(1, len(components)): # components[0] is always empty
            name = components[i]

            # For each component, we check if it exists in the current node's dictionary.
            # Only create a new node when 1) this is the last component; 2) there is no such component yet
            if name not in cur.map:
                if i == len(components) - 1:
                    cur.map[name] = TrieNode(name)
                else:
                    return False
            cur = cur.map[name]

        # Value not equal to -1 means the path already exists in the trie.
        if cur.value != -1:
            return False

        cur.value = value
        return True

    #  Returns the value associated with path or returns -1 if the path doesn't exist.
    def get(self, path: str) -> int:
        # Obtain all the components
        cur = self.root
        # Start "curr" from the root node.
        components = path.split("/")

        # Iterate over all the components.
        for i in range(1, len(components)):

            # For each component, we check if it exists in the current node's dictionary.
            name = components[i]
            if name not in cur.map:
                return -1
            cur = cur.map[name]
        return cur.value

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
