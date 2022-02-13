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



