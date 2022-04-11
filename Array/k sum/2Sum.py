# O(n) for both time and space complexity
# Array is not sorted, so use hashset is faster. Sorting costs nlogn
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        for i, num in enumerate(nums):
            if target - num in index_map:
                return [index_map[target - num], i]
            else:
                index_map[num] = i
