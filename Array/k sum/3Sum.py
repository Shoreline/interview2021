# Time: O(nlogn + n^2) = O(n^2)
# space: depending on the sorting algorithm. Python's sort() is O(n)? Merging sort?
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()
        res = []

        for low in range(len(nums) - 2):
            if low > 0 and nums[low] == nums[low - 1]:  # avoid duplicates
                continue

            mid = low + 1
            high = len(nums) - 1
            while mid < high:
                if mid > low + 1 and nums[mid] == nums[mid - 1]:  # avoid duplicates
                    mid += 1
                    continue

                sum1 = nums[low] + nums[mid] + nums[high]
                if sum1 == 0:
                    res.append([nums[low], nums[mid], nums[high]])
                    mid += 1
                    high -= 1
                elif sum1 < 0:
                    mid += 1
                else:
                    high -= 1

        return res
