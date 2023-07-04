# 115: [1,10,100,101,102,..,109,11,110,111,...,115,12,13 ...19, 2, 20, 21, ...99]
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []

        def helper(val):
            if val > n:
                return

            res.append(val)
            helper(val * 10)
            if val % 10 < 9:
                helper(val + 1)

        helper(1)
        return res

# class Solution:
#     def lexicalOrder(self, n: int) -> List[int]:
#         res = []
#         cur = 1
#         for i in range(n): # add n numbers
#             # Add the current number to the result
#             res.append(cur)
#             # If the current number times 10 is still less than or equal to n, move to the next level
#             # need to handle 10, 11, ... first, before adding 2, 3, 4... to res[]
#             if cur * 10 <= n:
#                 cur *= 10
#             # Otherwise, move to the next number at the current level
#             else:
#                 # If we've reached the end of a level, divide by 10 to go back up one level
#                 if cur >= n:
#                     cur //= 10
#                 cur += 1
#                 # Skip over any trailing zeroes (e.g. if cur = 19, skip over 190, 191, 192, etc.)
#                 # while cur % 10 == 0:
#                 #     cur //= 10
#         return res