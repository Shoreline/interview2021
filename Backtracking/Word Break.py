# 1) Backtracking + memoization
# time: O(n^3), size of recursion tree can go up to n^2
# space: O(n)
from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = frozenset(wordDict)

        @lru_cache(None)
        def breakable(word):
            for i in range(len(word)):
                if i == 0 and word in word_set:
                    return True
                elif breakable(word[:i]) and breakable(word[i:]):
                    return True

            return False
        
        return breakable(s)
    
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         word_set = frozenset(wordDict)

#         @lru_cache
#         def helper(s: str, start: int):
#             if start == len(s):
#                 return True
#             for end in range(start + 1, len(s) + 1):
#                 if s[start:end] in word_set and helper(s, end):
#                     return True
#             return False

#         return helper(s, 0)

# 2) DP
# dp[i]: the first i chars of input string can be broken or not. dp[0] = true
# there are len(s) chars, so len(dp) = len(s) + 1
# Use a set to save wordDict

# time: O(n^3),  two nested loops, and substring computation at each iteration costs O(n).
# space: O(n)
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         word_set = set(wordDict)
#         dp = [False] * (len(s) + 1)
#         dp[0] = True

#         # Check all substrings starting at i, see if they are breakable
#         for i in range(len(s) + 1):
#             if not dp[i]:
#                 continue    # The prerequisite is that the first i chars is breakable. Otherwise no need to check further.

#             # we can only try all possibilities
#             for j in range(i + 1, len(s) + 1):
#                 if s[i:j] in word_set: # s[i:j] cost O(n)
#                     dp[j] = True

#         return dp[-1]

# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         # breakable[i]: the first i characters of s can be broken or not
#         breakable = [False] * (len(s) + 1)
#         breakable[0] = True

#         for i in range(len(s) + 1):
#             if not breakable[i]:
#                 continue

#             for j in range(i + 1, len(s) + 1):
#                 if s[i:j] in wordDict:
#                     breakable[j] = True

#         return breakable[-1]
