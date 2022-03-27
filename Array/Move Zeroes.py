# Move non-zero elements to the front
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i, j = 0, 0
        while j < len(nums):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        return nums
