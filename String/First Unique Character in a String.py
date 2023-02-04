class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1

# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         chars = [-1]*26
#         for i in range(len(s)):
#             index = ord(s[i]) - ord('a')
#             chars[index] = i if chars[index] == -1 else -2
#
#         res = -1
#         for i in range(len(chars)):
#             if chars[i] >= 0:
#                 res = min(res, chars[i]) if res >= 0 else chars[i]
#         return res

# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         chars = [0]*26
#         for c in s:
#             chars[ord(c) - ord('a')] += 1

#         for i, c in enumerate(s):
#             if chars[ord(c) - ord('a')] == 1:
#                 return i
#         return -1


