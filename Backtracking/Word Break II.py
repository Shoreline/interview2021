# copied
# Backtracking with partial results cached
# 1.Every time, we check whether s starts with a word. If so, we check whether the substring s[len(word):] starts with a word, etc.
# 2.resultOfTheRest keeps calling until we hit the last word. If the last word is in the dict, we append it to res.
# The last word is 'dog ==> 'res = [ "dog"]
# 3. This time, we skip "else," since we fulfill the condition " if len(word) == len(s)." We store it in memo: {'dog': ['dog']}
# 4.Then we return to "resultOfTheRest = self.helper(s[len(word):], wordDict, memo)"

# Time complexity: O(n^3). Size of recursion tree can go up to n^2. The creation of the 'res' List takes n time.

# 1) use lru_cache() as the memory
from functools import lru_cache


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        @lru_cache(None)
        def helper(s: str) -> List[str]:
            if not s:  # if s is empty
                return []

            res = []
            for word in wordDict:
                if not s.startswith(word):
                    continue
                if len(word) == len(s):  # find an exact match
                    res.append(word)
                else:
                    resultOfTheRest = helper(s[len(word):])
                    for item in resultOfTheRest:
                        item = word + ' ' + item  # add current word back to the head of each item
                        res.append(item)
            return res

        return helper(s)

# 2) Use our own map as the memory
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
#         return self.helper(s, wordDict, {})

#     # memo is a map of <substring, wb_result>
#     def helper(self, s, wordDict, memo)-> List[str]:
#         if s in memo:
#             return memo[s]
#         if not s: # if s is empty
#             return []

#         res = []
#         for word in wordDict:
#             if not s.startswith(word):
#                 continue
#             if len(word) == len(s): # find an exact match
#                 res.append(word)
#             else:
#                 resultOfTheRest = self.helper(s[len(word):], wordDict, memo)
#                 for item in resultOfTheRest:
#                     item = word + ' ' + item # add current word back to the head of each item
#                     res.append(item)
#         memo[s] = res
#         return res

# other thoughts: Trie tree problem?