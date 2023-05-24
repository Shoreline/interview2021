# DFS (backtracking)
# Time complexity: O(4^N *N), 4 is referring to the maximum value length in the hash map, N is the length of digits
# 4^N combinations (worst case) of strings generated, and for each of those combinations you have to actually construct
# the string. Constructing a string of N length is an O(N) operation. So thus 4^N * N.

# Space complexity: O(N), where N is the length of digits.
# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         if (len(digits) == 0):
#             return []
#
#         # Map all the digits to their corresponding letters
#         kb_map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
#                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
#         res = []
#         self.dfs(digits, 0, kb_map, '', res)
#         return res
#
#     def dfs(self, digits: str, pos: int, kb_map, tmp: str, res: List[str]):
#         if (pos >= len(digits)):
#             res.append(tmp)
#             return
#
#         letters = kb_map[digits[pos]]
#         for i in range(len(letters)):
#             tmp += letters[i]
#             self.dfs(digits, pos + 1, kb_map, tmp, res)
#             tmp = tmp[:-1]  # remove the last element of tmp
#         return

import json

haha = "{ “2022-06-11”: {  “ios”: {   “pageViewCount”: 20000   “unique”: 12999  },  “reddit web”: {   “pageViewCount”: 20000   “unique”: 12999  } } }"

p = json.loads(haha)

print(p)