# Keep computing the next ugly number till hitting the n-th ugly number
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2, i3, i5 = 0, 0, 0  # the indices of the most recent 2/3/5-related ugly number
        for i in range(n - 1):  # the first number is already initialized in ugly[], so only need to loop n-1 times
            u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
            umin = min(u2, u3, u5)
            if umin == u2:
                i2 += 1
            if umin == u3:  # can't use elif
                i3 += 1
            if umin == u5:  # can't use elif
                i5 += 1
            ugly.append(umin)

        return ugly[-1]
