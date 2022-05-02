# 3 iterations. Time: O(n); Space O(1)
# If integer i exists, let nums[i-1] has negative value. Note that the absolute value of nums[i-1] shall be kept.
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 1st iteration, setting all irrelevant elements to 0
        # After this loop, all elements in nums are non-negative
        for i in range(len(nums)):
            if nums[i] < 1 or nums[i] > len(nums):
                nums[i] = 0

        # 2nd iteration, for each integer found at found_int = nums[i], flipping nums[found_int - 1] to be negative
        # After this iteration, nums[i] > 0? {i+1 exist in original nums} : {i+1 doesn't exist in original nums}
        for i in range(len(nums)):
            if nums[i] == 0:
                continue

            found_int = abs(nums[i])  # abs(nums[i]) is found_int. Set nums[fount_int - 1] to negative
            if (nums[found_int - 1] == 0):  # free to use
                nums[found_int - 1] = -found_int
            else:
                nums[found_int - 1] = -abs(
                    nums[found_int - 1])  # keeps the integer saved in nums[index], but marking it as negative

        # 3rd iteration, find the first missing positive
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1

        # Corner case: if nums has all first len(nums) integers, the first missing integer is len(nums) + 1
        return len(nums) + 1