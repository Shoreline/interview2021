# Sliding window
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, j = 0, 0
        sum = 0
        res = len(nums) + 1

        while j < len(nums):
            sum += nums[j]

            if sum >= target:
                while sum >= target:
                    res = min(res, j - i + 1)
                    sum -= nums[i]
                    i += 1
                if res == 1:
                    return res

            j += 1

        return res if res <= len(nums) else 0
