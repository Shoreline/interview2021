# Need a separate array.
# output[i] = (x0 * x1 * ... * xi-1) * (xi+1 * .... * xn-1)
# So two loops:
#   1) let output[i] = (x0 * x1 * ... * xi-1)
#   2) let output[i] *= (xi+1 * .... * xn-1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [0] * len(nums)
        tmp = 1
        for i in range(len(nums)):
            product[i] = tmp
            tmp *= nums[i]

        tmp = 1
        for i in range(len(nums) - 1, -1, -1):
            product[i] *= tmp
            tmp *= nums[i]

        return product