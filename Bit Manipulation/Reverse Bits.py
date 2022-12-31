# integer is unsigned
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32): # shift res 32 times to capture all 32-bits of n. In the end, res it is 33-bit
            last_bit = n & 1
            res += last_bit
            res <<= 1
            n >>= 1

        res >>= 1   # shift back res one bit
        return res

# Build a reversed number by keep retriving the last bit of n
# class Solution:
#     def reverseBits(self, n: int) -> int:
#         res, pos = 0, 31  # 32-bit
#         while pos >= 0:
#             last_bit = n & 1
#             res += (last_bit << pos)
#
#             n = n >> 1
#             pos -= 1
#
#         return res

# class Solution:
#     def reverseBits(self, n: int) -> int:
#         res = n & 1
#         n >>= 1
#         for i in range(31): # shift 31 times, so in total 32-bit
#             res <<= 1
#             last_bit = n & 1
#             res += last_bit
#             n >>= 1
#
#         return res