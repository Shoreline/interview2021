class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for c in columnTitle:
            val = ord(c) - ord('A') + 1
            res = res * 26 + val
        return res

# class Solution:
#     def titleToNumber(self, columnTitle: str) -> int:
#         res = 0
#         for i in range(len(columnTitle)):
#             res *= 26
#             res += ord(columnTitle[i]) - ord('A') + 1
#         return res
