# Sliding window
# count the number of zeroes in current window.
# Keep expanding window towards right, then #_zeros is too high, shrink the window from left.
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        left, right = 0, 0
        zeroes = 0

        while right < len(nums):
            if nums[right] == 0:  # found a new zero
                zeroes += 1

            while zeroes == 2:  # if there are too many zeroes in current window, shrink from left
                if nums[left] == 0:
                    zeroes -= 1
                left += 1

            res = max(res, right - left + 1)  # update the biggest window length
            right += 1  # expand our window towards right

        return res
