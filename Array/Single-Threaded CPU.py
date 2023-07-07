class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        # sort tasks by 1) starting time; 2) ending time; 3) original_index
        tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])

        h = []  # heap of (ending_time, original_index)
        cur_time = tasks[0][0]  # The CPU shall work once there is available tasks

        res = []
        i = 0
        while len(res) < len(tasks):
            # push all tasks starting at / before cur_time
            # sort by smallest ending_time (shortest processing time) and original_index
            while i < len(tasks) and tasks[i][0] <= cur_time:
                heapq.heappush(h, (tasks[i][1], tasks[i][2]))  # (processing_time, original_index)
                i += 1

            # We only want to process the first task in heap. Then update the time and continue while loop.
            if h:
                processing_time, original_index = heapq.heappop(h)
                cur_time += processing_time
                res.append(original_index)
            elif i < len(tasks):  # if there is no task in heap, move time to the next unfinished task
                cur_time = tasks[i][0]
        return res        