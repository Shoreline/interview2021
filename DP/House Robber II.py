# Reuse House robber I.
# two situations:
#   1) never rob the last house;
#   2) never rob the first house

# Or:
#   1) rob the first house, and never rob the last one;
#   2) do not rob the first house, and possible to rob the last one.

# Same dp function, just different initial status
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        # Never rob the last house
        dp1 = 0
        dp2 = 0
        for i in range(len(nums) - 1):
            tmp = max(dp1 + nums[i], dp2)
            dp1 = dp2
            dp2 = tmp
        res1 = dp2

        # Never rob the first house
        dp1 = 0
        dp2 = 0
        for i in range(1, len(nums)):
            tmp = max(dp1 + nums[i], dp2)
            dp1 = dp2
            dp2 = tmp
        res2 = dp2

        return max(res1, res2)

# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         # case 1: rob the first house
#         dp1 = nums[0]
#         dp2 = 0
#         res1 = dp1
#         for i in range(1, len(nums) - 1):
#             res1 = max(dp1, dp2 + nums[i])
#             dp1, dp2 = res1, dp1
#
#         # case 2: do not rob the first house
#         dp1 = 0
#         dp2 = 0
#         res2 = 0
#         for i in range(1, len(nums)):
#             res2 = max(dp1, dp2 + nums[i])
#             dp1, dp2 = res2, dp1
#
#         return max(res1, res2)
