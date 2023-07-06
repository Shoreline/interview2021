class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        return nums


class Solution2:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            if not res:
                res.append(num)
            else:
                res.append(num + res[-1])

        return res