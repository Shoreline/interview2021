# Greedy
# Sorty intervals by ending time

# Always pick the interval with the earliest end time. Then you can get the maximal number of non-overlapping
# intervals. (or minimal number to remove). This is because, the interval with the earliest end time produces the
# maximal capacity to hold rest intervals.
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        cur_end = float('-inf')
        res = 0

        for start, end in intervals:
            if start >= cur_end:  # no overlap
                cur_end = end
            else:  # there is an overlap. Remove this interval of [start, end], cur_end stays the same.
                res += 1

        return res
