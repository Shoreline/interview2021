# !BFS + DFS
# PS asks to return path, so a simple visited set of nodes is not sufficient.
# Level-by-level scanning, and use a parents (or children) map<str, list[str]> to store the parents/children from one word to a list of words during the BFS traverse.
# Label visited nodes at level granulairty, instead of individually (one-by-one)
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        if endWord not in wordList:
            return []

        # BFS traverse
        cur_lvl = {beginWord}
        # A helper map that saves the transisition paths during our BFS traverse.
        # map<str, list[str]>.
        children = collections.defaultdict(list)

        while cur_lvl:
            wordList -= cur_lvl  # Remove visited nodes for the whole level
            next_lvl = set()

            for word in cur_lvl:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i + 1:]
                        if new_word in wordList:
                            next_lvl.add(new_word)
                            children[word].append(new_word)

            # Must finish building the whole next_lvl, then check if endWord has been found.
            # Can't stop as long as the endWord is found, otherwise will the result may not be complete.
            if endWord in next_lvl:
                break
            cur_lvl = next_lvl

        # DFS reconstruction
        res = []

        def dfs(word: str, tmp: list[str]):
            if word == endWord:
                res.append(tmp[:])
                return

            for child_word in children[word]:
                tmp.append(child_word)
                dfs(child_word, tmp)
                tmp.pop()

        dfs(beginWord, [beginWord])
        return res

    # Use parents instead of children
# class Solution:
#     def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
#         wordList = set(wordList)
#         if endWord not in wordList:
#             return []

#         # BFS traverse
#         cur_lvl = {beginWord}
#         # A helper map that saves the transisition paths during our BFS traverse.
#         # map<str, list[str]>.
#         parents = collections.defaultdict(list)

#         while cur_lvl:
#             wordList -= cur_lvl # Remove visited nodes for the whole level
#             next_lvl = set()

#             for word in cur_lvl:
#                 for i in range(len(word)):
#                     for c in 'abcdefghijklmnopqrstuvwxyz':
#                         new_word = word[:i] + c + word[i+1:]
#                         if new_word in wordList:
#                             next_lvl.add(new_word)
#                             parents[new_word].append(word)

#             # Must finish building the whole next_lvl, then check if endWord has been found.
#             # Can't stop as long as the endWord is found, otherwise will the result may not be complete.
#             if endWord in next_lvl:
#                 break
#             cur_lvl = next_lvl

#         # DFS reconstruction
#         res = []
#         def dfs(word:str, path:list[str]):
#             if word == beginWord:
#                 path.append(word)
#                 res.append(path[::-1])
#             else:
#                 for p_word in parents[word]:
#                     dfs(p_word, path + [word])

#         dfs(endWord, [])
#         return res


# Wrong solution: can return one result, but not necessarily all the results.
# from collections import deque
# class Solution:
#     def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

#         words = set(wordList)
#         queue = deque([(beginWord, [beginWord])])

#         res = []
#         while queue:
#             w, seq = queue.popleft()
#             if w == endWord:
#                  res.append(seq[:])

#             for i in range(26):
#                 c = chr(ord('a') + i)

#                 for j in range(len(w)):
#                     new_w = w[:j] + c + w[j+1:]
#                     if new_w not in words:
#                         continue
#                     words.remove(new_w)
#                     queue.append((new_w, seq[:] + [new_w]))

#         return res




