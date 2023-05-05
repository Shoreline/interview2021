class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c_index = {}  # all seen characters' latest index
        # note that c_index can contain characters not in current longest substring

        cur_start = 0
        ans = 0
        for i, c in enumerate(s):
            # c in c_index doesn't necessarily mean c will be a character in the current longest substring
            if c in c_index and cur_start <= c_index[c]:
                cur_start = c_index[c] + 1
            ans = max(ans, i - cur_start + 1)
            c_index[c] = i
        return ans

# Same O(n)
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         c_index = {}
#         res = 0
#         cur = 0
#         for i, c in enumerate(s):
#             if c not in c_index:
#                 cur += 1
#                 res = max(res, cur)
#             else:
#                 for j in range(i - cur, c_index[c]):
#                     c_index.pop(s[j])
#                     cur -= 1
#
#             c_index[c] = i
#
#         return res