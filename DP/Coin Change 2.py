# Combination sum problem
# Switched the inner/outer sequence of the for loops, as in combination sum IV (the permutation sum version of this problem.)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for amt in range(amount + 1):
                # one way to get amt from amt - coin: amt - coin + coin
                # So if there is dp[amt-coin] ways to come up amt - coin;
                #   then there dp[amt] = sigma(dp[amt-coin]), while coin is every type of coin denomination
                if amt - coin >= 0:
                    dp[amt] += dp[amt - coin]
        return dp[amount]
