# dp[i]: maximum money for nums[0] - nums[i] houses
# dp[i] = max(dp[i-1], nums[i] + dp[i-2])
#   Either rob nums[i]: nums[i] + dp[i-2]; or not rob nums[i]: dp[i-1]

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp1 = 0 # dp[i-1]
        dp2 = 0 # dp[i-2]
        for i in range(len(nums)):
            tmp = max(dp1, dp2 + nums[i])
            dp1, dp2 = tmp, dp1

        return dp1

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
