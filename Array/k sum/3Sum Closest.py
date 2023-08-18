# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is
# closest to target.
#
# Return the sum of the three integers.
#
# You may assume that each input would have exactly one solution.
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        for low in range(len(nums)):
            mid, high = low + 1, len(nums) - 1
            while mid < high:
                sum = nums[low] + nums[mid] + nums[high]
                if sum == target:
                    return sum
                elif abs(target - sum) < abs(diff):
                    diff = target - sum

                if sum < target:
                    mid += 1
                else:
                    high -= 1

        return target - diff