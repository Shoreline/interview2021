# Sliding window
# It's a subarray sum problem, but we do not use prefix sum this time.
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, j = 0, 0
        res = len(nums) + 1
        sub_sum = 0

        while j < len(nums):
            sub_sum += nums[j]
            while sub_sum >= target:
                res = min(res, j - i + 1)
                # if res == 1:
                #     return 1

                sub_sum -= nums[i]
                i += 1
            j += 1

        return res if res <= len(nums) else 0
