# Binary search
# low + high may cause integer overflow for some languages, but not python3

# If target is not to be found: we end up with low < high and nums[high] < target < nums[left]. In this case,
# target shall be inserted to nums[left]
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return low