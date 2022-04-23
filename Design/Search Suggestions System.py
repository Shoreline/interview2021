# Note that we are told to return ALL suggestions while typing each char of the search word.
#   Typing a new char -> building a new prefix
#   So if the search word has n chars, then there are 7 prefixes, and we shall return a list[list[string]] of len = 7
#   Even if there is no suggestion after some char in search word, an empty list[] still need to be added.

# Solution 1: Binary search
# Sort the input products[] list.
# For a prefix to have suggestion, then the immediate next elements must in the sorted products[]

# For example, if A[i] is a prefix of A[j],
# A[i] must be the prefix of A[i + 1], A[i + 2], ..., A[j]
import bisect


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res, prefix, i = [], '', 0
        for c in searchWord:
            prefix += c
            i = bisect.bisect_left(products, prefix, i)

            # check the next 3 words
            tmp = []
            for w in products[i:i + 3]:
                if w.startswith(prefix):
                    tmp.append(w)
            res.append(tmp)
            # Equivalent to:
            # res.append([w for w in products[i:i + 3] if w.startswith(prefix)])

        return res

# Solution 2: Trie tree
# Save a list of words to each Trie node, they are the suggestions of that node
# class TrieNode:
#     def __init__(self):
#         self.children = dict()
#         self.words = []

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word):
#         node = self.root
#         for char in word:
#             if char not in node.children:
#                 node.children[char] = TrieNode()
#             node = node.children[char]
#             node.words.append(word)
#             node.words.sort()

#             # we are told to only keep the 3 lexicographically minimums words
#             while len(node.words) > 3:
#                 node.words.pop()

#     def search(self, word):
#         res = []
#         node = self.root
#         for char in word:
#             if char not in node.children:
#                 break
#             node = node.children[char]
#             res.append(node.words[:])

#         # If there is no suggestions since some char in the search word,
#         # still add empty lists to the result
#         for _ in range(len(word) - len(res)):
#             res.append([])
#         return res

# class Solution:
#     def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
#         trie = Trie()
#         for word in products:
#             trie.insert(word)
#         return trie.search(searchWord)
