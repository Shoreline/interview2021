from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # Count the char frequency in t
        # Counter is a subclass of dict that’s specially designed for counting hashable objects in Python.
        # Counter helps generate a character counting map with one line.
        remaining_chars = Counter(t)

        min_len = float('inf')
        left, right = 0, 0  # s[left] to s[right] (inclusive) are the start/end char of current substring (or s[left:right + 1])
        word_count = 0  # number of valid characters in t exist in the cur substring
        res_start = 0

        for right in range(len(s)):
            if s[right] not in remaining_chars:  # if char is not in t -> not interested, continue
                continue

            remaining_chars[s[right]] -= 1  # values in remaining_chars can be negative.
            if remaining_chars[s[right]] >= 0:  # only increment word_count when t still have remaining number of this char
                word_count += 1

            # all chars in t have been found in current substring: try shrinking the substring from the left-hand side
            while word_count == len(t):
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    res_start = left

                if s[left] in remaining_chars:
                    remaining_chars[s[left]] += 1

                    # No need to always decrement word_count, unless remaining_chars[s[left]] > 0
                    if remaining_chars[s[left]] > 0:
                        # this will break the while loop. Making [left, right+1] has one missing character of t
                        word_count -= 1

                left += 1

        if min_len <= len(s):
            return s[res_start: res_start + min_len]
        else:
            return ''
