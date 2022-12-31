# Reconstruct the number that only shows once bit-by-bit
# Let x0, x1, ... x_k be the i-th bit of the numbers showing up 3 times. And y be the i-th bit of the number showing
# only once. Then to get y we can sum up all the i-th bits from all numbers, then modulo by 3:
#   (3 * x0 + 3 * x1 + ... 3 * x_k+ y) % 3
#   Since x_k is either 0 or 1, so 3 * x_k is either 0 or 3, so (3 * x_k) % 3 it is always 0
#   -> (3 * x0 + 3 * x1 + ... 3 * x_k+ y) % 3  = 0 + 0 + ... + y = y

# 1. Iterate over all possible 32 bits. And for each num check if this num has non-zero bit on position i
#       (with num & (1<<i) == (1<<i) formula)
# 2. We evaluate this sum modulo 3. Note, that in the end for each bit we can have either 0 or 1 and never 2.
# 3. Next, update our answer single with evaluated bit.
# 4. Finally, we need to deal with overflow cases in python: maximum value for int32 is 2^31 - 1
#       So if we get number more than this value we have negative answer in fact.
#
# Complexity: time complexity is O(32n),
#   which may be not fully honest linear, but is fine for the purpose of this problem.
#   If we want just O(n) complexity, I think problem becomes not medium but hard. Space complexity here is O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = 0
        for i in range(32):
            count = 0
            for num in nums:
                if num & (1 << i) == (1 << i):  # check if num has non-zero bit on position i
                    count += 1
            single += ((count % 3) << i)

        # return single if single < (1<<31) else single - (1<<32)
        return single if single <= 2 ** 31 - 1 else single - (2 ** 32)