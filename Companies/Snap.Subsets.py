# input: an array of numbers, and an integer k
# output: total number of subsets such that max(subset) + min(subset) < k
# [3, 2, 1, 4] and k = 4
# output: 2 [(2,1), (1)]

# All we need is to find that two max and min items. Other items can be freely inserted into the subset.
#
# Pick n' out of n items
# Permutation combos: n! / (n - n')!
# Combination combos: n! / [(n - n')! * n'!]
def subsets(nums, k):
    nums.sort()
    res = 0

    # optional, for exporting the actual subsets
    # T(2 ^ n)
    sets = []
    def bt(start, stop, tmp):
        tmp.append(nums[stop])
        sets.append(tmp[:])
        tmp.pop()
        for pos in range(start, stop):
            if pos > start and nums[pos] == nums[pos - 1]: # de-duplicate
                continue
            tmp.append(nums[pos])
            bt(pos + 1, stop, tmp)
            tmp.pop()


    for i in range(len(nums)):
        # corner case: one-item subset of nums[i].
        if nums[i] * 2 < k:
            res += 1

        for j in range(i + 1, len(nums)):
            # all combinations having nums[i] and nums[j] qualify the condition
            # subset = [ nums[i], nums[j], others]
            # others: whether to pick any item between nums[j] and nums[i]
            #   2 possibilities (pick or not pick) for each item;
            #   there are j - i - 1 items
            #   => there are 2 ^ (j - i - 1)
            #   Note that items must be unique! If not, use an additional prefix_sum array to count unique_items so far?
            if nums[i] + nums[j] < k:
                res += pow(2, j - i - 1)

                bt(i+1, j, [nums[i]]) # optional



    return res


print(subsets([3, 2, 1, 4], 4))



from typing import List
# t: o(n * 2^n): call dfs 2^n times, each time deepcopy takes n
# s: o(n * 2^n) (to save all result)
# For subset, don't wait till pos == len(nums) to add tmp[] to res[]
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def bt(pos: int, tmp: list[int]):
            # 1) add none of the remaining elements
            res.append(tmp[:])
            # 2) add one of the remaining elements and continue bt
            for i in range(pos, len(nums)):
                tmp.append(nums[i])
                bt(i + 1, tmp)
                tmp.pop()

        bt(0, [])
        return res

# time: O(n * 2^n) : dfs is called 2^n times, each time a deep copy takes O(n)
# space: O(n) : recursion stack is at most O(n) deep. (output storage is not considered)
class Solution2:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def bt(tmp: List[int], pos: int):
            res.append(tmp[:])

            for i in range(pos, len(nums)):
                # each round, only process the first one of the duplicated chars
                # Next round, will process the 2nd of the duplicated chars, and so on so forth
                if i > pos and nums[i] == nums[i - 1]:
                    continue
                tmp.append(nums[i])
                bt(tmp, i + 1)
                tmp.pop()

            return

        nums.sort()
        res = []
        bt([], 0)
        return res