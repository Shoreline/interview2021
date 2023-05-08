class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        counter = 0
        for num in nums:
            counter += seen[num-k] + seen[num+k]
            seen[num] += 1
        return counter

# class Solution:
#     def countKDifference(self, nums: List[int], k: int) -> int:
#         c = Counter(nums)
#         res = 0
#         for num in c:
#             res += c[num + k] * c[num]
#             res += c[num - k] * c[num]
#
#         return res // 2