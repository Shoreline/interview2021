# O(n) for both time and space complexity
# Array is not sorted, so use hashset is faster. Sorting costs nlogn
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_to_index_map = {}
        for i, val in enumerate(nums):
            if target - val in val_to_index_map:
                return [i, val_to_index_map[target - val]]
            else:
                val_to_index_map[val] = i
