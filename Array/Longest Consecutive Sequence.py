class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0

        for num in nums:
            if num not in nums_set:
                continue

            val = num
            cur_len = 0
            while val in nums_set:
                cur_len += 1
                nums_set.remove(val)
                val += 1

            val = num - 1  # corner case
            while val in nums_set:
                cur_len += 1
                nums_set.remove(val)
                val -= 1

            res = max(res, cur_len)

        return res

# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         nums_set = set()
#         for num in nums:
#             nums_set.add(num)

#         max_len = 0
#         for num in nums:
#             if num in nums_set:
#                 cur_len = 0
#                 tmp = num
#                 while tmp in nums_set:
#                     nums_set.remove(tmp)
#                     cur_len += 1
#                     tmp -= 1
#                 tmp = num + 1
#                 while tmp in nums_set:
#                     nums_set.remove(tmp)
#                     cur_len +=1
#                     tmp +=1
#                 max_len = max(cur_len, max_len)

#         return max_len