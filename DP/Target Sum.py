# Similar to Coin Change 2.
#   But simpler, since all elements have to be used (+ or -). But in Coin 2, each type of coin can be used 0 - n times.
# The DP solution using array of size 2001 works since the constraits are restricted. If nums[i] > 2000 etc then that DP solution won't work

# Another DP from the forum
# counter[x]: counts how many ways to get amount x
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        counter = Counter({0: 1})  # important initial value

        for num in nums:
            new_counter = Counter()
            for shown_amt in counter:
                new_counter[shown_amt + num] += counter[shown_amt]
                new_counter[shown_amt - num] += counter[shown_amt]
            counter = new_counter
        return counter[target]

# TLE (brute force)
# O(2^n) time, O(n) space (depth of the recursion tree can go upto n)
# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         counter = [0]
#         self.dfs(nums, target, 0, counter)
#         return counter[0]

#     def dfs(self, nums:List[int], target: int, pos: int, counter:List[int]) -> None:
#         if pos == len(nums) and target == 0:
#             counter[0] += 1
#         if pos >= len(nums):
#             return

#         self.dfs(nums, target - nums[pos], pos + 1, counter)
#         self.dfs(nums, target + nums[pos], pos + 1, counter)

#         return