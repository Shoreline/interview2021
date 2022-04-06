# Bottom up DP
# Bit manipulation trick of n & (n - 1)
#   - Flip the last significant 1 (not necessary the last bit) in n to be 0.
#   - say n = xxxxx100, then n' =  n & (n-1) = xxxxx000
#   - In summary, after this trick, n' will have 1 less 1-bit than n
# dp[i] saves the 1-bit counts of integer i
# dp[i] = dp[ i & (i - 1)] + 1 = dp[i'] + 1
# i' must be some value <= than i
#   - Interesting dp[i] function. Combined index operation and value change (+1)
#   - Obviously, i >= i'
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n+1):
            ans[i] = ans[i & (i-1)] + 1
        return ans