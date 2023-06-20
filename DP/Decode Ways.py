# /*
#  * Be careful about how to handle initial status: set them both to 1!
#  *
#  * The two if blocks are parallel, not nested.
#  */
# dp[i]: how many decode ways for the s[:i+1] characters (from s[0] to s[i], inclusive).
# dp[i]= dp[i-1] + dp[i-2]; But note that only eligible dp[i-1] and dp[i-2] can be added
from functools import lru_cache


class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':  # corner case!
            return 0
        dp1 = 1  # 1 way to decode the first 0 char
        dp2 = 1  # still 1 way to decode the first char

        for i in range(1, len(s)):
            dp3 = 0  # dp[i] of the next round

            # s[i] is a valid number, so we can add valid decoding ways before s[i]
            if int(s[i]) > 0:
                dp3 += dp2

            # s[i-1] + s[i] is a valid number, so we can add valid decoding ways before s[i-1]
            if 10 <= int(s[i - 1:i + 1]) <= 26:
                dp3 += dp1

            dp1 = dp2
            dp2 = dp3

        return dp2


class Solution2:

    @lru_cache(maxsize=None)
    def helper(self, pos, s) -> int:
        # If you reach the end of the string
        # Return 1 for success.
        if pos == len(s):
            return 1
        # If the string starts with a zero, it can't be decoded
        elif s[pos] == '0':
            return 0
        elif pos == len(s) - 1:
            return 1

        res = self.helper(pos + 1, s)
        if 10 <= int(s[pos: pos + 2]) <= 26:
            res += self.helper(pos + 2, s)

        return res

    def numDecodings(self, s: str) -> int:
        return self.helper(0, s)
