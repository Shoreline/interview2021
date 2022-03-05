# integer is unsigned
# Build a reversed number by keep retriving the last bit of n
class Solution:
    def reverseBits(self, n: int) -> int:
        res, pos = 0, 31  # 32-bit
        while pos >= 0:
            last_bit = n & 1
            res += (last_bit << pos)

            n = n >> 1
            pos -= 1

        return res