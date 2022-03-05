# Reverse (math)
# 1) reverse the whole array first
# 2) reverse first k % len(nums) elements
# 3) reverse the remaining elements
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverseSubArray(start: int, end: int) -> None:
            i = 0
            while start + i < end - i:
                nums[start + i], nums[end - i] = nums[end - i], nums[start + i]
                i += 1

        if len(nums) <= 1 or k == 0:
            return
        pos = k % len(nums)  # corner case
        reverseSubArray(0, len(nums) - 1)
        reverseSubArray(0, pos - 1)
        reverseSubArray(pos, len(nums) - 1)
