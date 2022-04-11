# T: O(unique_chars * n). Since there are maximum 26 unique characters: O(26*n) -> O(n)

# There can be [1, 26] unique chars in the longest substring
#   26 can be further reduced by the length of set(s)
# Find the longest substring for all 26 cases, and do max() -> do 26 sliding windows run
# class Solution:
#     def longestSubstring(self, s: str, k: int) -> int:
#         result = 0
#         for T in range(1, len(set(s))+1):
#             # [start, end) is the longest substring
#             start, end, unique_chars, repeat_enough_chars, freq,  = 0, 0, 0, 0, [0]*26
#             while end < len(s):
#                 if unique_chars <= T:
#                     c = ord(s[end]) - 97
#                     freq[c] += 1
#                     if freq[c] == 1:
#                         unique_chars += 1
#                     if freq[c] == k:
#                         repeat_enough_chars += 1
#                     end += 1
#                 else:
#                     c = ord(s[start]) - 97
#                     if freq[c] == k:
#                         repeat_enough_chars -= 1
#                     freq[c] -= 1
#                     if freq[c] == 0:
#                         unique_chars -= 1
#                     start += 1

#                 if unique_chars == T and repeat_enough_chars == T:
#                     result = max(result, end - start)

#         return result

# A very simple solution, but takes O(n^2) in the worst case. Actually, it runs faster than the O(26n) solution above
# Recursivly split s on the less frequent chars, and check each substrings if their chars have enough frequency.
# "ababacb"
# 3
#   -> after the first round: [ababa, b]
import re  # regular expression library. Need to use re.split()


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        less_frequent_chars = [c for c in set(s) if s.count(c) < k]
        if not less_frequent_chars:
            return len(s)
        else:
            spliters = '|'.join(less_frequent_chars)
            return max(self.longestSubstring(t, k) for t in re.split(spliters, s))        