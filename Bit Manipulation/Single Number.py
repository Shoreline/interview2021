# x ^ x = 0; x ^ 0 = x; XOR is associative and commutative
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(1, len(nums)):
            res ^= nums[i]
        return res