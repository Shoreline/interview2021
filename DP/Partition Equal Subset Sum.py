# Improved, just 1d bottom-up DP
# Time: O(sum(nums)//2 * len(nums)); space: O(sum(nums)//2)
# If any non-empty subset of nums[] can sum up to sum(nums)//2, then canPartition = True
# dp[i]: can any non-empty subset of nums[] sum up to equal i
# dp[i] = dp[i] or dp[i - a_num] : either not let a_num in that subset, or let a_num in that subset.
#
# Note: nums contains only positive integers
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False
        sub_sum = total_sum // 2

        dp = [False] * (sub_sum + 1)
        dp[0] = True
        for num in nums:
            for i in range(sub_sum, -1, -1):  # start from sub_sum instead of 1. avoid reusing num in each i-loop
                # for i in range(1, sub_sum + 1): # wrong! In this way, we basically allow using num multiple times in the subset
                # since dp[i] depends on dp[j] where j < i, so to avoid resuing num, start from behind.
                if i - num >= 0:
                    dp[i] = dp[i] or dp[i - num]  # when i - num = 0 then dp[j-num] is surely true
                if dp[sub_sum]:
                    return True

        return False

# 2d DP
# Hard since each dimension has totally different meanings
# dp[i][j]: Can the first i elements in nums (num[0] ~ num[i-1]) sum up to get j. Therefore j_max = sub_sum and i_max = len(nums)
# dp[i][j] = dp[i - 1][j] || dp[i-1][j - nums[i]]
#   - Either don't use nums[i-1] but can still get j with nums[0] ~ nums[i-2]; or use nums[i], then needs dp[i-1][j - nums[i-1]] to be true
# dp[0][0] = True

# Can partition: any subset of nums[] can sum up to total_sum/2
# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         total_sum = sum(nums)
#         if total_sum % 2 == 1:
#             return False

#         sub_sum = total_sum // 2
#         dp = [[False] * (sub_sum + 1) for _ in range(len(nums) + 1)]
#         dp[0][0] = True
#         for i in range(1, len(dp)):
#             for j in range(len(dp[0])):
#                 if j >= nums[i-1]:
#                     dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i-1]]
#                 else:
#                     dp[i][j] = dp[i-1][j]

#         return dp[-1][-1]