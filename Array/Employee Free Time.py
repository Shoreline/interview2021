"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # sort all intervals by starting time
        ints = sorted([i for s in schedule for i in s], key=lambda x: x.start)
        #print([str(i.start) + " " + str(i.end) for i in ints])
        res, end = [], ints[0].end
        for i in ints[1:]:
            if i.start > end: # if stats after the maximum ending time, there is a free period
                res.append(Interval(end, i.start))
            end = max(end, i.end)
        return res        