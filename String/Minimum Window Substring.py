# Sliding window
# Keep incrementing right until all chars in target has been included. Then start shrinking left until the substring no
# more includes all target characters.
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # Count the char frequency in t
        # Counter is a subclass of dict that’s specially designed for counting hashable objects in Python.
        # Counter helps generate a character counting map with one line.
        target_c_count = Counter(t)

        min_len = float('inf')
        # s[left] to s[right] (inclusive) are the start/end char of current substring (or s[left:right + 1])
        left, right = 0, 0
        included_target_chars = 0  # number of valid characters in t exist in the cur substring
        res_start = 0

        for right in range(len(s)):
            if s[right] not in target_c_count:  # if char is not in t -> not interested, continue
                continue

            target_c_count[s[right]] -= 1  # values in target_c_count can be negative.
            # only increment included_target_chars when t still have remaining number of this char
            if target_c_count[s[right]] >= 0:
                included_target_chars += 1

            # all chars in t have been found in current substring: try shrinking the substring from the left-hand side
            while included_target_chars == len(t):
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    res_start = left

                if s[left] in target_c_count:
                    target_c_count[s[left]] += 1

                    # No need to always decrement included_target_chars, unless target_c_count[s[left]] > 0
                    if target_c_count[s[left]] > 0:
                        # this will break the while loop. Making [left, right+1] has one missing character of t
                        included_target_chars -= 1

                left += 1

        return s[res_start: res_start + min_len] if min_len <= len(s) else ''
