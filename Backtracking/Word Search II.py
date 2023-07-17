# Build a TrieTree with the given words
# DFS to find a match

# ["oath","pea","eat","rain"]
# -> trie form: {'o': {'a': {'t': {'h': {'$$': 'oath'}}}}, 'p': {'e': {'a': {'$$': 'pea'}}}, 'e': {'a': {'t': {'$$': 'eat'}}}, 'r': {'a': {'i': {'n': {'$$': 'rain'}}}}}
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        END_OF_WORD = '$$'  # any string with >1 character works

        # TrieNode is simplified from a custom class to a <char, <char, {char, <...>>>> map
        #   Specially, TrieNode.isEndofWord = True is represented by having a k-v pair of {END_OF_WORD, word}
        trie_root = {}  # root of trie tree
        for word in words:
            node = trie_root
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            # mark the existence of a word in trie node
            node[END_OF_WORD] = word

        rowNum = len(board)
        colNum = len(board[0])

        res = []

        def dfs(row, col, root):
            if row < 0 or row >= rowNum or col < 0 or col >= colNum:
                return

            c = board[row][col]
            if c not in root:
                return

            cur_node = root[c]  # we have checked that c is in parent before calling dfs()

            # check if we find a match of word
            if END_OF_WORD in cur_node:
                res.append(cur_node[END_OF_WORD])
                cur_node.pop(END_OF_WORD)  # avoid adding duplicated items to res

            # Label the cell as visited
            board[row][col] = '.'
            for (d1, d2) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                dfs(row + d1, col + d2, cur_node)
                # Restore the cell
            board[row][col] = c

            # If cur_node is empty, meaning it is a matched leaf node (cur_node[END_OF_WORD] has been poped out)
            # We can remove it since it is useless in future. This way the size of the Trie can be reduced in future.
            # Helps reducing the workload of search in future.
            if not cur_node:
                root.pop(c)

        for row in range(rowNum):
            for col in range(colNum):
                dfs(row, col, trie_root)

        return res

    # # Trie classes are copied from https://leetcode.com/problems/implement-trie-prefix-tree/
# class TrieNode:
#     def __init__(self):
#         self.children = [None] * 26 # Problem statement says lowercase letters only
#         self.isWordEnd = False

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word: str) -> None:
#         ptr = self.root
#         for c in word:
#             if not ptr.children[ord(c) - ord('a')]:
#                 ptr.children[ord(c) - ord('a')] = TrieNode()

#             ptr = ptr.children[ord(c) - ord('a')]
#         ptr.isWordEnd = True
#         return

# # not needed in this problem
# #     def search(self, word: str) -> bool:
# #         ptr = self.root
# #         for c in word:
# #             if not ptr.children[ord(c) - ord('a')]:
# #                 return False
# #             ptr = ptr.children[ord(c) - ord('a')]
# #         return ptr.isWordEnd

# #     def startsWith(self, prefix: str) -> bool:
# #         ptr = self.root
# #         for c in prefix:
# #             if not ptr.children[ord(c) - ord('a')]:
# #                 return False
# #             ptr = ptr.children[ord(c) - ord('a')]
# #         return True

# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         res = []
#         trie = Trie()
#         for word in words:
#             trie.insert(word)

#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 self.dfs(i,j, board, trie.root, "", res)

#         return res

#     def dfs(self, i:int, j:int, board: List[List[str]], node: TrieNode, path: str, res: List[str]):
#         if node.isWordEnd:
#             res.append(path)
#             node.isWordEnd = False # remove this word from the Trie
#             # return can't return here

#         if 0 <= i < len(board) and 0<=j <len(board[0]) and board[i][j] != '*':
#             next_node = node.children[ord(board[i][j]) - ord('a')]
#             if not next_node:
#                 return

#             tmp = board[i][j]
#             path += board[i][j]
#             board[i][j] = '*'
#             self.dfs(i+1, j, board, next_node, path, res)
#             self.dfs(i-1, j, board, next_node, path, res)
#             self.dfs(i, j+1, board, next_node, path, res)
#             self.dfs(i, j-1, board, next_node, path, res)
#             board[i][j] = tmp

#         return
