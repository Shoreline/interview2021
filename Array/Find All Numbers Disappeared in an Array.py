class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        count = Counter(nums)
        for i in range(1, len(nums) + 1):
            if i not in count:
                res.append(i)
        return res