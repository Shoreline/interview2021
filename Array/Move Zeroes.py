# Move non-zero elements to the front
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pos = 0
        # Move non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1

        # Set remaining list to zero
        for i in range(pos, len(nums)):
            nums[i] = 0

# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         i, j = 0, 0
#         while j < len(nums):
#             if nums[j] != 0:
#                 nums[i], nums[j] = nums[j], nums[i]
#                 i += 1
#             j += 1
#         return nums
