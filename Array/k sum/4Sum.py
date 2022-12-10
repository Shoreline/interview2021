# T: O(n^3)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        if (len(nums) < 4):
            return res

        nums.sort()

        i = 0
        for i in range(len(nums) - 3):  # -3: there can be 3 elements after i
            if i > 0 and nums[i] == nums[i - 1]:  # avoid duplicates
                continue

            for j in range(i + 1, len(nums) - 2):  # -2: there can be 2 elements after j
                if j > i + 1 and nums[j] == nums[j - 1]:  # avoid duplicates
                    continue

                m = j + 1
                n = len(nums) - 1
                while m < n:
                    if m > j + 1 and nums[m] == nums[m - 1]:  # avoid duplicates
                        m += 1
                        continue
                    sum1 = nums[i] + nums[j] + nums[m] + nums[n]
                    if sum1 == target:
                        res.append([nums[i], nums[j], nums[m], nums[n]])
                        m += 1
                        n -= 1
                    elif sum1 < target:
                        m += 1
                    else:
                        n -= 1
        return res


# General solution for kSum problems.
#
# Time: O(n^3). For kSum(), the time is O(n^(k-1)) when k>=3, so 5Sum is O(n^4)
# Space: O(n). O(k) for recursion, worst case k = n
class Solution_gen:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            res = []

            if len(nums) < k:
                return []
            elif k == 2:
                return twoSum(nums, target)
            else:
                for i in range(len(nums)):
                    if i > 0 and nums[i] == nums[i - 1]:
                        continue
                    # After picking nums[i], all possible combinations of the remaining k-1 numbers
                    remaining_combos = kSum(nums[i + 1:], target - nums[i], k - 1)
                    for rem_combo in remaining_combos:
                        res.append([nums[i]] + rem_combo)  # list concat

            return res

        def twoSum(nums:List[int], target:int) -> List[List[int]]:
            res = []
            i, j = 0, len(nums) - 1
            while i < j:
                if i > 0 and nums[i] == nums[i-1]:
                    i+=1
                    continue
                sum = nums[i] + nums[j]
                if sum == target:
                    res.append([nums[i], nums[j]])
                    i += 1
                    j -= 1
                elif sum < target:
                    i += 1
                else:
                    j -= 1
            return res

        nums.sort()
        return kSum(nums, target, 4)
