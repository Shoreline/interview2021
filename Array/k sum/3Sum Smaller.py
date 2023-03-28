# Ask for the number of non-duplicated index triplets.
#   Just the number, not actual triplets
#   index, not value (index naturally won't duplicate)
# T: O(n^2)

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                val = nums[i] + nums[j] + nums[k]
                if val < target:
                    # All [i, j, k], [i, j, k - 1], ...[i, j, j+1] < target
                    res += k - j
                    j += 1
                else:
                    k -= 1

        return res