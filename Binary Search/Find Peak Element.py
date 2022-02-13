# Binary search
# Note that nums[-1] and nums[n] are considered -inf. So it is ensured there is at least one peak in nums
# nums can be seen as being made up of ascending or descending sequences
# ascending -> peak is at the rightmost; descending -> leftmost
# Compare nums[mid] and nums[mid+1], find if they are in ascending or descending, and can eliminate half elements.
#
# Consider any given sequence in nums array as alternating ascending and descending sequences.
# For each ascending sequence (nums[i] <= nums[i+1]) -> there is a peak on the right side (somewhere >= i + 1)
# similar for decending sequence, there is a peak on the left side (somewhere <= i)

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:  # at least two elements are between left and right
            mid = left + (right - left) // 2

            # nums[mid] is in a descending sequence. Since left < right, so mid + 1 is surly within range
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:  # nums[mid] is in a asencidng sequence
                left = mid + 1

        return left
