# top-down dp
# T: O(target * len(nums)), space: O(target)
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res = 0
        
        @lru_cache(None)
        def dfs(target):
            if target == 0:
                return 1
            if target < 0:
                return 0
            
            res = 0
            for i in range(len(nums)):
                res += dfs(target - nums[i])
            return res
        
        return dfs(target)

# Bottom-up DP. Same time and space complexities.
# This is actually PermutationSum. Check Coin Change 2, the true combination sum version.
# dp[i]: number of different permutations to sum up to value i
# dp[i]: sigma(dp[i - num]), while i - num >= 0 (num is every element in nums)
# The answer is dp[target]
# T: O(target * len(nums)); S: O(target)

# Can each num in nums be used multiple times?
# Does sequence of an answer matter? (Is [1,2] the same as [2,1]?)
#   - If no then it is a combination problem. If yes, it is actually a permutation problem.
# class Solution:
#     def combinationSum4(self, nums: List[int], target: int) -> int:
#         dp = [0] * (target + 1)
#         dp[0] = 1

#         for i in range(target + 1):
#             for n in nums:
#                 if i - n >= 0:
#                     dp[i] += dp[i - n]

#         return dp[-1]
