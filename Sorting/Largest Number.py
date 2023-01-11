# sorting problem.
# sort n1 and n2 by each digit
# - can also be done by let x and y be numbers in string format. And compare their concatenated results
# Note that python3 does not support cmp = compare in sort() anymore (can work around by import functools)
# This solution uses the build-in sort(). We can also write our own quicksort function.

import functools


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def comparator(x, y):
            return 1 if x + y > y + x else -1

        str_nums = [str(num) for num in nums]
        str_nums.sort(key=functools.cmp_to_key(comparator), reverse=True)
        return '0' if str_nums[0] == '0' else ''.join(str_nums)

# Don't use functools
# class LargerNumKey(str):
#     def __lt__(x: str, y: str):
#         return x + y > y + x  # x and y are numbers in string format. Here are compare their concatenated results
#
#
# class Solution:
#     def largestNumber(self, nums: List[int]) -> str:
#         # largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
#         # return '0' if largest_num[0] == '0' else largest_num # largest_num can be "00"
#
#         nums_str = [str(num) for num in nums]
#         nums_str.sort(key=LargerNumKey)
#         if nums_str[0] == '0':  # corner case: when all nums elements are 0
#             return '0'
#         else:
#             return ''.join(nums_str)
