class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # If a value exist, mark nums[value - 1] as negative
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])

        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i + 1)

        return res

# class Solution:
#     def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
#         res = []
#         unique_nums = set(nums)
#         for i in range(1, len(nums) + 1):
#             if i not in unique_nums:
#                 res.append(i)
#         return res