# DP with memorization
# DP[i]: the min palindrome partitions of substring s[i:]
# DP[i] = 1 + min(all DP[j]), where j>=i and s[i:j+1] is a palindrome
# T: O(N^3)
#   There is N states in dp, they are dp(0), dp(1)...dp(n), each state we need a loop O(N) to calculate the result,
#   so total O(N^2). isPalindrome() takes O(N)
# S: O(N)

class Solution:
    def minCut(self, s: str) -> int:

        # dp(pos): the minimum cuts needed to make all pieces in s[pos:] palindrome
        @lru_cache(None)
        def dp(pos) -> int:
            res = float('inf')
            for i in range(pos + 1, len(s) + 1):  # so the biggest i is len(s)
                first_part = s[pos:i]
                if first_part == first_part[::-1]:
                    # corner case: when i == len(s), the whole s[pos:] is already a palindrome and needs 0 cut
                    res = min(res, 1 + dp(i) if i != len(s) else 0)
            return res

        return dp(0)

    # class Solution:
#     def minCut(self, s: str) -> int:
#         n = len(s)
#
#         def isPalindrome(s: str) -> bool:
#             return s == s[::-1]
#
#         # Returns the min palindrome partitions of substring s[i:]
#         @lru_cache(None)
#         def dp(i):  # s[i..n-1]
#             if i == n:
#                 return 0  # substring is a single letter, no need to further cut
#             res = math.inf
#             for j in range(i + 1, n + 1):
#                 if isPalindrome(s[i:j]):
#                     res = min(res, 1 + dp(j))
#             return res
#
#         return dp(0) - 1

    # class Solution:
#     def minCut(self, s: str) -> int:
#         n = len(s)

#         @lru_cache(None)
#         def isPalindrome(l, r):  # l, r inclusive
#             if l >= r: return True
#             if s[l] != s[r]: return False
#             return isPalindrome(l+1, r-1)

#         # Returns the min palindrome partitions of substring s[i:]
#         @lru_cache(None)
#         def dp(i):  # s[i..n-1]
#             if i == n:
#                 return 0    # substring is a single letter, no need to further cut
#             res = math.inf
#             for j in range(i, n):
#                 if (isPalindrome(i, j)):
#                     res = min(res, 1 + dp(j+1))
#             return res

#         return dp(0) - 1