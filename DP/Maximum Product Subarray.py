# DP
# T: O(n); S: O(1)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -sys.maxsize

        # local_min/max: the min/max product subarray from nums[0] to nums[i], and nums[i] must be included
        local_min = nums[0]
        local_max = nums[0]
        global_max = nums[0]

        for i in range(1, len(nums)):  # i starts from 1
            # new_local_max must includes i. old local_max/local_min must includes i-1.
            # So new_local_max can be built in this way
            new_local_max = max(nums[i], local_min * nums[i], local_max * nums[i])
            new_local_min = min(nums[i], local_min * nums[i], local_max * nums[i])

            global_max = max(global_max, new_local_max)
            local_min = new_local_min
            local_max = new_local_max

        return global_max
