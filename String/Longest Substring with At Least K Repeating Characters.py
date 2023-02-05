# T: O(unique_chars * n). Since there are maximum 26 unique characters: O(26*n) -> O(n)

# Find the size of the longest substring that contains exactly x unique characters, each showed at least k times.
#   1 <= x <= 26.
# There can be [1, 26] unique chars in the longest substring
#   26 can be further reduced by the length of set(s)
# Find the longest substring for all 26 cases, and do max() -> do 26 sliding windows run

# If all #unique_chars is the same as #chars_repeated_enough, then we found a qualified substring.
# class Solution:
#     def longestSubstring(self, s: str, k: int) -> int:
#         result = 0
#         total_unique_chars = len(set(s))
#         for T in range(1, total_unique_chars + 1):
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
# Recursively split s on the less frequent chars, and check each substrings if their chars have enough frequency.
# "ababacb"
# 3
#   -> after the first round: [ababa, b]

# If every character appears at least k times, the whole string is ok. Otherwise split by one of the less frequent
# character (because it will always be too infrequent and thus can't be part of any ok substring) and make the most
# out of the splits.
#
# In cases where we perform split at every index, the maximum depth of recursive call could be O(N). For each recursive
# call it takes O(N) time to build the countMap resulting in O(n^2) time complexity.
#
# Space Complexity: O(N). This is the space used to store the recursive call stack.
# The maximum depth of recursive call stack would be O(N).
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        char_count = Counter(s)
        for char, count in char_count.items():
            if count < k:
                return max(self.longestSubstring(piece, k) for piece in s.split(char))
        return len(s)

# class Solution:
#     def longestSubstring(self, s: str, k: int) -> int:
#         for c in set(s):
#             if s.count(c) < k:
#                 return max(self.longestSubstring(t, k) for t in s.split(c))
#         return len(s)

# import re  # regular expression library. Need to use re.split()
# class Solution:
#     def longestSubstring(self, s: str, k: int) -> int:
#         if len(s) < k:
#             return 0
#         less_frequent_chars = [c for c in set(s) if s.count(c) < k]
#         if not less_frequent_chars:
#             return len(s)
#         else:
#             spliters = '|'.join(less_frequent_chars)
#             return max(self.longestSubstring(t, k) for t in re.split(spliters, s))