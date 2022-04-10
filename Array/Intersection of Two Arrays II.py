# count(num1) then iterate through num2
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = Counter(nums1)
        res = []
        for n in nums2:
            if n in counter1 and counter1.get(n) > 0:
                counter1[n] -= 1
                res.append(n)
        return res

