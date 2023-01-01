# DP
# T: O(n);
# S O(1): Just need to save two variables
# Say dp[i] is the ways to reach the i-th step, then dp[i] = dp[i-1] + dp[i-2]
# This is because to reach i-th step, one can either jump from i-1, or i-2.

class Solution:
    def climbStairs(self, n: int) -> int:
        dp1 = 1  # to reach step 0
        dp2 = 1  # to reach step 1
        for i in range(2, n + 1):
            tmp = dp1 + dp2
            dp1 = dp2
            dp2 = tmp
        return dp2

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         # dp[i] = dp[i-1] + dp[i-2]
#         if n <= 2:
#             return n
#
#         pre_pre = 1  # star 1
#         pre = 2  # stair 2
#         res = 0
#         for i in range(2, n):
#             res = pre_pre + pre
#             pre_pre = pre
#             pre = res
#
#         return res

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if(n == 1):
#             return 1

#         prepreWays = 1
#         preWays = 1
#         ways = 0

#         i = 2 # start from the 2nd step
#         while i<=n:
#             ways = preWays + prepreWays

#             # prepre ways become pre ways next round
#             # pre ways become current ways next round
#             prepreWays = preWays
#             preWays = ways

#             i+=1

#         return ways


# class Solution:
#     def climbStairs(self, n: int) -> int:
#         # Say dp[i] is the ways to reach the i-th step, then dp[i] = dp[i-1] + dp[i-2]
#         # This is because to reach i-th step, one can either jump from i-1, or i-2.

#         if(n == 1):
#             return 1

#         preStepWays = 1
#         prePreStepWays = 1
#         ways = 0

#         for i in range(2, n+1):
#             ways = preStepWays + prePreStepWays

#             # prepre step ways become pre step ways next round
#             # pre step ways become current ways next round
#             prePreStepWays = preStepWays
#             preStepWays = ways

#         return ways
