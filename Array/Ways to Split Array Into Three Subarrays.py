class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        sz, res, j, k = len(nums), 0, 0, 0

        # get prefix sum
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]

        for i in range(sz - 2):
            while j <= i or (j < sz - 1 and nums[j] < nums[i] * 2):
                j += 1
            while k < j or (k < sz - 1 and nums[k] - nums[i] <= nums[-1] - nums[k]):
                k += 1
            res = (res + k - j) % 1000000007
        return res