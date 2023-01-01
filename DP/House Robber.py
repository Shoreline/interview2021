# dp[i]: maximum money for dp[0] - dp[i] houses
# dp[i] = max(dp[i-1], nums[i] + dp[i-2])

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp1 = 0
        dp2 = 0
        for i in range(len(nums)):
            tmp = max(dp1 + nums[i], dp2)
            dp1 = dp2
            dp2 = tmp
        return dp2

# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         dp1 = 0  # dp[i-1]
#         dp2 = 0  # dp[i-2]
#         res = nums[0]
#         for i in range(0, len(nums)):
#             res = max(dp1, nums[i] + dp2)
#             dp1, dp2 = res, dp1
#
#         return res
