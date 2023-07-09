"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

# T: O(n*log(k)), n is the number of tasks from all employees
#                 k is the number of employees
# S: O(k)
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # schedule is a 2d array
        # schedule[i][j]: the employee i, task j

        # collect first tasks of all employees
        heap = []
        for i, tasks in enumerate(schedule):
            # (task.start, employee index, task index)
            # sort primarily by starting time of tasks from all employees
            #   employee index is the tie-breaker
            # need task index to tell if there is still remaining unprocessed task in the list
            heapq.heappush(heap, (tasks[0].start, i, 0))

        res = []
        _, i, j = heap[0]
        prev_end = schedule[i][j].end
        while heap:
            _, i, j = heapq.heappop(heap)
            # check if there is still remaining unprocessed task of this employee, and push it to heap
            if j + 1 < len(schedule[i]):
                heapq.heappush(heap, (schedule[i][j + 1].start, i, j + 1))

            task = schedule[i][j]
            if task.start > prev_end: # if starts after the maximum ending time so far, there is a free period
                res.append(Interval(prev_end, task.start))
            prev_end = max(prev_end, task.end)
        return res

# O(nlogn)
class Solution2:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # Flatten the schedule into one list of intervals, sort all intervals by starting time
        ints = sorted([i for s in schedule for i in s], key=lambda x: x.start)
        # ints = sorted([[time_slot.start,time_slot.end] for employee in schedule for time_slot in employee])

        #print([str(i.start) + " " + str(i.end) for i in ints])
        res, end = [], ints[0].end
        for i in ints[1:]:
            if i.start > end: # if stats after the maximum ending time, there is a free period
                res.append(Interval(end, i.start))
            end = max(end, i.end)
        return res        