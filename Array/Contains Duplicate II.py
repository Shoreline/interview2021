# Keep a sliding window of k elements using Hash Table.
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True

            seen.add(nums[i])
            if i - k >= 0:
                seen.remove(nums[i - k])

        return False
