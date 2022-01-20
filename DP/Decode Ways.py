# /*
#  * Be careful about how to handle initial status: set them both to 1!
#  *
#  * The two if blocks are parallel, not nested.
#  */
# dp[i]: how many decode ways for the first i characters.
# dp[i]= dp[i-1] + dp[i-2]; But note that only eligible dp[i-1] and dp[i-2] can be added
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':  # corner case!
            return 0
        dp1 = 1  # 1 way to decode the first 0 char
        dp2 = 1  # still 1 way to decode the first char

        for i in range(1, len(s)):
            dp3 = 0  # dp[i] of the next round

            # s[i] is a valid number, so we can add valid decodings before s[i]
            if int(s[i]) > 0:
                dp3 += dp2

            # s[i-1:i+1] is a valid number, so we can add valid decodings before s[i-1]
            if 10 <= int(s[i - 1:i + 1]) <= 26:
                dp3 += dp1

            dp1 = dp2
            dp2 = dp3

        return dp2