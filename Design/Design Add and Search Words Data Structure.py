# Trie tree
# Sometimes TLE
class TrieNode:
    def __init__(self):
        self.charmap = {}
        self.endChar = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        ptr = self.root
        for c in word:
            if c not in ptr.charmap:
                ptr.charmap[c] = TrieNode()
            ptr = ptr.charmap[c]
        ptr.endChar = True

    def search_helper(self, word: str, root: TrieNode) -> bool:
        ptr = root
        for i in range(len(word)):
            if word[i] in ptr.charmap:
                ptr = ptr.charmap[word[i]]
            elif word[i] == '.':
                for node in ptr.charmap.values():
                    if self.search_helper(word[i + 1:], node):
                        return True
                return False
            else:
                return False

        return ptr.endChar

    def search(self, word: str) -> bool:

        return self.search_helper(word, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)