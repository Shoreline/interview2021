# 1. Count how many 1s in the array (c)
# 2. Run a sliding window of size c, return the window has the least amount of 0s
#
#   2.1: iterate the whole nums[], also from beginning
# T O(n), S O(1)
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones = nums.count(1)
        cur_zeros = nums[:ones].count(0)
        res = cur_zeros
        for i in range(ones, len(nums) + ones): # go back to beginning after reaching the end
            i = i if i < len(nums) else i % len(nums)
            if nums[i] == 0:
                cur_zeros += 1
            if nums[i - ones] == 0:
                cur_zeros -= 1
            res = min(res, cur_zeros)

        return res

# 1. Count how many 1s in the array (c)
# 2. Extend nums to be nums + nums, then same as "Minimum Swaps to Group All 1's Together"
# 3. Run a sliding window of size c, return the window has the least amount of 0s
# T O(n), S O(n)
# class Solution:
#     def minSwaps(self, nums: List[int]) -> int:
#         ones = nums.count(1)
#         cur_zeros = nums[:ones].count(0)
#         nums = nums + nums

#         res = cur_zeros
#         for i in range(ones, len(nums)):
#             if nums[i] == 0:
#                 cur_zeros += 1
#             if nums[i - ones] == 0:
#                 cur_zeros -= 1
#             res = min(res, cur_zeros)

#         return res