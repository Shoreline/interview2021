# Sliding window
# Works for k most distinct characters.
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        # <char, last_seen_index>
        distinct_chars = collections.defaultdict(int)
        distinct_chars[s[0]] = 0
        left, right = 0, 0
        res = 1
        while right < len(s):
            if len(distinct_chars) < 2 or s[right] in distinct_chars:
                distinct_chars[s[right]] = right
            else:
                index_to_remove = min(distinct_chars.values())
                left = distinct_chars.pop(s[index_to_remove]) + 1
                distinct_chars[s[right]] = right

            res = max(res, right - left + 1)
            right += 1

        return res

# class Solution:
#     def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
#         if not s:
#             return 0
#
#         # map<char, count> in the sliding window
#         char_count = collections.defaultdict(int)
#         start, end = 0, -1
#         res = 0
#         for i, c in enumerate(s):
#             char_count[c] += 1
#             end += 1
#
#             if len(char_count) > 2:
#                 for j in range(start, i):
#                     char_count[s[j]] -= 1
#                     if char_count[s[j]] == 0:
#                         del char_count[s[j]]
#                         start = j + 1
#                         break
#             res = max(res, end - start + 1)
#
#         return res

