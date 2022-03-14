# TrieNode class has a set that saves all child TrieNodes, and bool isWordEnd
# Trie tree class only has one memeber field: a TrieNode which is the root of the trie tree; 3 functions: insert/search and startWith.
class TrieNode:
    def __init__(self):
        self.children = [None] * 26  # Problem statement says lowercase letters only
        self.isWordEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        ptr = self.root
        for c in word:
            if not ptr.children[ord(c) - ord('a')]:
                ptr.children[ord(c) - ord('a')] = TrieNode()

            ptr = ptr.children[ord(c) - ord('a')]
        ptr.isWordEnd = True
        return

    def search(self, word: str) -> bool:
        ptr = self.root
        for c in word:
            if not ptr.children[ord(c) - ord('a')]:
                return False
            ptr = ptr.children[ord(c) - ord('a')]
        return ptr.isWordEnd

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        for c in prefix:
            if not ptr.children[ord(c) - ord('a')]:
                return False
            ptr = ptr.children[ord(c) - ord('a')]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)