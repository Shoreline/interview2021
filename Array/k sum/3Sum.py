# Ask for non-duplicated value triplets (not index triplest!)
# Time: O(nlogn + n^2) = O(n^2)
# space: depending on the sorting algorithm. Python's sort() is O(n)? Merging sort?
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()
        res = []

        for low in range(len(nums) - 2):
            # avoid duplicates
            if low > 0 and nums[low] == nums[low - 1]:
                continue

            mid = low + 1
            high = len(nums) - 1
            while mid < high:
                # avoid duplicates
                # No need to do the same for nums[high]. Because after de-duplicating nums[low] and nums[mid], the sum
                # of next nums[low] + nums[mid_2] must be different from sum(nums[low], nums[mid]), meaning that there
                # can only have a different nums[high]
                if mid > low + 1 and nums[mid] == nums[mid - 1]:
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
