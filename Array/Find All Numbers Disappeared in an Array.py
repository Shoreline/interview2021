class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        unique_nums = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in unique_nums:
                res.append(i)
        return res