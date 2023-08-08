# We are told that all elements in nums are within [lower, higher]
# /*
#  * cannot just do "if not nums return []" at the beginning, but return [lower -> upper]
#  */
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        # missing ranges are valid values within lower / upper
        # so use lower - 1, upper + 1 instead of simply lower / upper
        nums = [lower - 1] + nums + [upper + 1]
        res = []

        # Only react when there is a gap (nums[i+1] - nums[i] > 1)
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1] - 1:
                res.append([nums[i] + 1, nums[i + 1] - 1])

        # for i in range(len(nums)-1):
        #     if nums[i+1] - nums[i] == 2: # Gap is only 1, so no need to use "->"
        #         res.append(str(nums[i]+1))
        #     elif nums[i+1] - nums[i] > 2: # Gap is more than 1, need to use "->"
        #         res.append(str(nums[i]+1)+'->'+str(nums[i+1]-1))

        return res
