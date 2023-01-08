# Find a pattern
'''
from up to down, then left to right
(let each integer be exactly one bit different from its neighbors)
0   1   11  110
        10  111
            101
            100

start:      [0]
i = 0:      [0, 1]
i = 1:      [0, 1, 3, 2]
i = 2:      [0, 1, 3, 2, 6, 7, 5, 4]
-> result for i is [result of i - 1] + 2^i * [result of i - 1]
'''
class Solution:
    def grayCode(self, n: int) -> List[int]:
        results = [0]
        for i in range(n):
            tmp = []
            for x in reversed(results):
                tmp.append( x + pow(2, i))
            results += tmp
        return results

# class Solution:
#     def grayCode(self, n: int) -> List[int]:
#         results = [0]
#         for i in range(n):
#             results += [x + pow(2, i) for x in reversed(results)]
#         return results