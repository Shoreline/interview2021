class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def bt(used_indice, tmp):
            if len(tmp) == len(nums):
                res.append(tmp[:])
                return
            for i in range(len(nums)):
                # If meet a duplicate, do not use it until its predecessor has been used -> make sure for a set of duplicate elements, only one sub-permutation will be used: the first one, the second one, ... the last one
                if i in used_indice or (i > 0 and nums[i] == nums[i-1] and (i-1) not in used_indice):
                    continue
                used_indice.add(i)
                tmp.append(nums[i])
                bt(used_indice, tmp)
                tmp.pop()
                used_indice.remove(i)
        bt(set(), [])
        return res
