# prefix sum
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        sum_front, sum_back = 0, sum(nums)
        res, diff, n = 0, float('inf'), len(nums)

        for i in range(n):
            sum_front += nums[i]
            sum_back -= nums[i]

            avg_front = sum_front // (i + 1)
            avg_back = sum_back // (n - i - 1) if n - i - 1 != 0 else 0

            if abs(avg_back - avg_front) < diff:
                diff = abs(avg_back - avg_front)
                res = i

        return res
