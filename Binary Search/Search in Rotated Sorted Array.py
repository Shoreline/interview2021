# Binary search
# Time: O(logN); space O(1)
# Slicing the rotated sorted array, there is guaranteed that one half is perfectly sorted.
# All numbers are unique, so the numbers in the sorted half has no overlapping with the other half.
# If target is not within the range of the sorted half, it can only be in the other half.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2

            if target == nums[mid]:
                return mid

            if nums[mid] >= nums[low]:  # left half is sorted
                # Reverse thinking: give the only case target is on the left; then all else cases the target must be
                # on the right
                if nums[low] <= target < nums[mid]:  # if target's index is in [low, mid)
                    high = mid - 1
                else:
                    low = mid + 1
            else:  # right half is sorted
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1
