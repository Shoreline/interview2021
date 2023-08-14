# Sliding window
# PS: k >= 0, and nums[i] is a positive integer
# Note that we want the number of CONTIGUOUS subarrays
#   sliding window, move j forward:
#   -> For every new found qualified subarray [nums[i], ..., nums[j]], we can see that
#   [nums[i+1], ... num[j]], [nums[i+2], ..., num[j]] are also qualified
#   There are j - i + 1 such arrays
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0
        prod = 1
        res = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            res += right - left + 1
        return res
