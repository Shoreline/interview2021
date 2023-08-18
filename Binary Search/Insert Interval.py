# O(N)
# Use binary search to find the place to insert the newInterval based on interval[0], then classic intervals merging.
#   Binary search doesn't need to care interval[k][1], only interval[k][0]
#   Classic intervals merging: insert new interval to a target index; then start merging from intervals[1]
from bisect import bisect


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        # Find a place to insert the newInterval, keep intervals sorted by interval[0]
        left = bisect.bisect_left(intervals, newInterval)
        # OR, write your own binary search function
        # left, right = 0, len(intervals) - 1
        # res = 0
        # while left <= right:
        #     mid = left + (right - left) // 2
        #     if newInterval[0] == intervals[mid][0]:
        #         left = mid
        #         break
        #     elif newInterval[0] < intervals[mid][0]:
        #         right = mid - 1
        #     else:
        #         left = mid + 1

        insert_index = left

        # Merge the interested intervals
        intervals.insert(insert_index, newInterval)
        res = [intervals[0][:]]

        for i in range(1, len(intervals)):
            if res[-1][-1] >= intervals[i][0]:
                res[-1][-1] = max(res[-1][-1], intervals[i][1])
            else:
                res.append(intervals[i])

        return res
