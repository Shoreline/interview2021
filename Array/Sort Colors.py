class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # i: first index that nums[i] is not surely 0 (except at the very beginning, most of the time i is the first
        # index of 1)
        # #j: (backward) first index that nums[k] is not surely 2

        # pos: nums[pos] is the next element hasn't been checked, also is the first index that is not surely 1
        i, pos, j = 0, 0, len(nums) - 1
        while pos <= j:
            if nums[pos] == 0:
                nums[pos], nums[i] = nums[i], nums[pos]  # nums[i] has been checked before (even when i=pos=0)
                i += 1
                pos += 1  # easy to miss.
            elif nums[pos] == 2:
                nums[pos], nums[j] = nums[j], nums[pos]
                j -= 1
            else:
                pos += 1

        return
