# There is a statement that any number can be represented as sum of 4 squares:
# https://en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem.
class Solution:
    def numSquares(self, n: int) -> int:
        num_set, i = set(), 1
        while i ** 2 <= n:
            num_set.add(i ** 2)
            i += 1

        # one-sum O(N^(1/2))
        if n in num_set:
            return 1

        # two-sum O(N)
        for n1 in num_set:
            if n - n1 in num_set:
                return 2

        # three-sum O(N)
        for n1 in num_set:
            for n2 in num_set:
                if n - n1 - n2 in num_set:
                    return 3

        # four-sum O(1)
        return 4

# TLE
# Time: O(n * sqrt n); space: O(N)
# Note that sqrt(n) is not an O(1) operation
# dp[i]: the minimum number of perfect square numbers which sum to i. So returns dp[n]
# dp[0] is not used at all.
# Initialize all dp[i*i] = 1 when i*i <=n first

# while i + j * j <=n:
#   dp[i + j*j] = min(dp[i + j*j], dp[i] + 1)
# - Why dp[i]+1? Since j*j is one square number, so we only need to worry the square number of i, which is saved in
#   dp[i]
# class Solution:
#     def numSquares(self, n: int) -> int:
#         dp = [n + 1] * (n + 1)  # initial value is higher than the maximum possible
#         i = 1
#         while i * i <= n:
#             dp[i * i] = 1
#             i += 1
#
#         for i in range(1, n + 1):  # o(n)
#             j = 0
#             while i + j * j <= n:  # o(sqrt(n))
#                 dp[i + j * j] = min(dp[i + j * j], dp[i] + 1)
#                 j += 1
#
#         return dp[n]

# class Solution:
#     def numSquares(self, n: int) -> int:
#         dp = [sys.maxsize] * (n + 1)
#         i = 1
#         while i * i < len(dp):
#             dp[i * i] = 1
#             i += 1
#
#         for i in range(1, len(dp)):
#             if dp[i] != sys.maxsize:
#                 k = 1
#                 while i + k * k < len(dp):
#                     dp[i + k * k] = min(dp[i + k * k], 1 + dp[i])
#                     k += 1
#
#         return dp[-1]

