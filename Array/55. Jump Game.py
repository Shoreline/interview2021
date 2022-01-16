# Check every element in nums, see if we can reach the ending index of nums.
# Time: O(n)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_pos = 0
        for i in range(len(nums)):
            max_pos = max(max_pos, i + nums[i])
            if (max_pos >= len(nums) - 1):
                return True
            elif i == max_pos:  # if reached the furthest index and still not end, then fail
                return False

        return False