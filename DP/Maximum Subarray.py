# /*
#  * 1D DP (reduced to just one variable to save space)
#
# cur_sum: sum of current subarray that includes nums[i]
# If cur_sum < 0, give up all elements in current subarray (by setting cur_sum = 0)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -float('inf')
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            res = max(res, cur_sum)
            if cur_sum < 0:
                cur_sum = 0

        return res

#  * local/global dp variables
#  *
#  * The maximum-subarray must ends with some A[i] So, let localMax[i] is the
#  * sub-maximum value of any sub array ends with A[i].
#  *
#  * Then for subarray ending with A[i+1], it has only two
#  * possibilities: 1) it contains A[i+1]: localMax[i+1] = localMax[i] + A[i+1]
#  * 2) it does not contain A[i+1]: localMax[i+1] = localMax[i]
#  */
# Time: O(n); Space: O(1)
# class Solution:
#     def maxSubArray(self, nums: list[int]) -> int:
#         local_max, global_max = nums[0], nums[0]
#
#         for i in range(1, len(nums)):
#             local_max = max(nums[i], local_max + nums[i])
#             global_max = max(global_max, local_max)
#
#         return global_max
