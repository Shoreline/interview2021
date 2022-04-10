class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1

# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         chars = [0]*26
#         for c in s:
#             chars[ord(c) - ord('a')] += 1

#         for i, c in enumerate(s):
#             if chars[ord(c) - ord('a')] == 1:
#                 return i
#         return -1


