# DFS (backtracking)
# Time complexity: O(4^N *N), 4 is referring to the maximum value length in the hash map, N is the length of digits
# 4^N combinations (worst case) of strings generated, and for each of those combinations you have to actually construct
# the string. Constructing a string of N length is an O(N) operation. So thus 4^N * N.

# Space complexity: O(N), where N is the length of digits.
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        # Map all the digits to their corresponding letters
        kb_map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                  "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []

        def bt(pos, tmp):
            if pos >= len(digits):
                res.append(''.join(tmp))
                return

            chars = kb_map[digits[pos]]
            for c in chars:
                tmp.append(c)
                bt(pos + 1, tmp)
                tmp.pop()

        bt(0, [])
        return res

# import json
#
# haha = "{ “2022-06-11”: {  “ios”: {   “pageViewCount”: 20000   “unique”: 12999  },  “reddit web”: {   “pageViewCount”: 20000   “unique”: 12999  } } }"
#
# p = json.loads(haha)
#
# print(p)