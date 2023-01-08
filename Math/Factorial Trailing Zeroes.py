# /*
# looking at the factors of two numbers: (factor: 因数, eg. 15 has two factors 3 and 5)
#  * The idea is that only 2x5 can generate a 0. And there are many more 2s than
#  * 5s. So just need to count how many factor of 5.
#  *
# Each number ending with 5 surely has a factor of 5
#  * Notice that 25, 125, 625,... offer more factor of 5s, so need to also add 5s in 25/5, 125/5, 625/5, ...
# 75 = 3*5*5 -> there are two factor of 5s
#  */
# T: O(logn), log is based on 5, not 2
# S: O(1)
class Solution:
    def trailingZeroes(self, n: int) -> int:
        five_factors = 0
        while n >= 5:
            five_factors += n // 5  # how many 5s in n
            n //= 5  # not n-1!

        return five_factors
