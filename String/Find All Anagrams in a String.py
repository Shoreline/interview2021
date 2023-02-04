# sliding window (fixed length) with two character counting maps
# Do maps comparison.
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        p_count = [0] * 26
        cur_count = [0] * 26

        for c in p:
            p_count[ord(c) - ord('a')] += 1

        res = []
        for i in range(len(s)):
            cur_count[ord(s[i]) - ord('a')] += 1
            if i >= len(p) - 1:
                # can simply use "==".
                # But if compare two maps, the equal condition is that they have identical key-value pairs. So for this
                # problem if to use maps, we need to delete a key once the value is 0
                if cur_count == p_count:
                    res.append(i - len(p) + 1)
                cur_count[ord(s[i - len(p) + 1]) - ord('a')] -= 1

        return res

# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         ans = []
#         char_count_p, char_count_cur = [0] * 26, [0] * 26
#
#         for char in p:
#             char_count_p[ord(char) - ord('a')] += 1
#
#         for i in range(len(s)):
#             char_count_cur[ord(s[i]) - ord('a')] += 1
#             if i >= len(p):
#                 char_count_cur[ord(s[i - len(p)]) - ord('a')] -= 1
#             # can simply use "==".
#             # But if compare two maps, the equal condition is that they have identical key-value pairs. So for this
#             # problem if to use maps, we need to delete a key once the value is 0
#             if char_count_cur == char_count_p:
#                 ans.append(i - len(p) + 1)
#
#         return ans


