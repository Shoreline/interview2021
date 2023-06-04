# solution I: same as Max Consecutive Ones II
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        left, right = 0, 0
        zeroes = 0

        while right < len(nums):
            if nums[right] == 0:  # found a new zero
                zeroes += 1

            while zeroes > k:  # if there are too many zeroes in current window, shrink from left
                if nums[left] == 0:
                    zeroes -= 1
                left += 1

            res = max(res, right - left + 1)  # update the biggest window length
            right += 1  # expand our window towards right

        return res


# solution II
# Since we have to find the MAXIMUM window, we never reduce the size of the window.
# We either increase the size of the window or remain same but never reduce the size.
#
class Solution2:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        for right in range(len(nums)):
            # If we included a zero in the window we reduce the value of k.
            # Since k is the maximum zeros allowed in a window.
            if nums[right] == 0:
                k -= 1
            # A negative k denotes we have consumed all allowed flips and window has
            # more than allowed zeros, thus increment left pointer by 1 to keep the window size same.
            if k < 0:
                # If the left element to be thrown out is zero we increase k.
                k += 1 - nums[left]
                left += 1

        return right - left + 1
