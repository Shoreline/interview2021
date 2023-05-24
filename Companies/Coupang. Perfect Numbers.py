# https://leetcode.com/discuss/interview-question/996283/coupang-oa-perfect-numbers
#  i,j >=1, m,n>=2  求 1-N 中 可以写成 i^m+j^n 的数量

# 1. Generate all x ^ y < N and save them to a set s
# 2. For i in s, if n - i is also in s then there is a match
import math
from functools import lru_cache


def perfectNumbers(n):

    s = set([1]) # all values that val is computed from i^m where i >= 1 and m >= 2 and val < n

    # For 1,000,000: maximum recursion depth exceeded in comparison
    # @lru_cache(None)
    # def genNums(x, y):
    #     if x ** y > n:
    #         return
    #
    #     s.add(x ** y)
    #     genNums(x + 1, y)
    #     genNums(x, y+1)
    # genNums(2, 2)

    # This works
    for x in range(2, int(math.sqrt(n)) + 1):
        y = 2
        while x ** y < n:
            s.add(x ** y)
            y += 1


    print("s size: ", len(s))
#    print(s)
    # Slow!
    # res = set()
    # for num in range(n+1):
    #     for i in s:
    #         if num - i in s:
    #             res.add(num)
    #             # num is already a perfect number. We don't need to return all possible ways to get one perfect number.
    #             break

    res = set()
    for x in s:
        for y in s:
            if x + y <= n:
                res.add(x + y)
            # else:
            #     break

    # print(len(res), len(res2))
    # print('res', res)
    # print('res2', res2)
    return res

#perfectNumbers(10)

#print(perfectNumbers(10))
# 1e6: 283676, takes ~20s to finish
print(len(perfectNumbers(1000000)))