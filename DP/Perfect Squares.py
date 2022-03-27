# Time: O(n * sqrt n); space: O(N)
# dp[i]: the minimum number of perfect square numbers which sum to i. So returns dp[n]
# dp[0] is not used at all.
# Initialize all dp[i*i] = 1 when i*i <=n first

# while i + j * j <=n:
#   dp[i + j*j] = min(dp[i + j*j], dp[i] + 1)
# - Why dp[i]+1? Since j*j is one square number, so we only need to worry the squre number of i, which is saved in dp[i]
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n + 1] * (n + 1)  # initial value is higher than the maximum possible
        i = 1
        while i * i <= n:
            dp[i * i] = 1
            i += 1

        for i in range(1, n + 1):  # o(n)
            j = 0
            while i + j * j <= n:  # o(sqrt(n))
                dp[i + j * j] = min(dp[i + j * j], dp[i] + 1)
                j += 1

        return dp[n]