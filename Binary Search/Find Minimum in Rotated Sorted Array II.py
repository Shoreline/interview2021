# Items are NOT unique!
# Not the same algo as looking for a specific value in rotated ordered array.
# If nums[i] is the smallest element in a rotated sorted array,
# Then   nums[i-1] > nums[i] -> to find nums[i] meaning to find somewhere nums[i-1] > nums[i]
# -> to find the non-sorted part

# worest case costs log(n) time
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + (high -low) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid if nums[high] != nums[mid] else high - 1
        return nums[low]        