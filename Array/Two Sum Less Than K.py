class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1
        res = -1
        while i<j:
            if nums[i]+nums[j] < k:
                res = max(res,nums[i]+nums[j])
                i += 1
            else:
                j -= 1
        return res        