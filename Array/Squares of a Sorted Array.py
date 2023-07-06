# PS: the input nums is sorted in non-decreasing order

# Two pointers
#   The next biggest squred num is either the leftmost or rightmost num
# O(n)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1

            result[i] = square * square
        return result

# O(nlogn)
class Solution2:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([num**2 for num in nums])