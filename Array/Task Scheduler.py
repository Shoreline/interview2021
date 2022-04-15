# total time = num_tasks + min_idle_time
#   min_idle_time = max_idle_time - fillable_tasks
#   max_idle_time = (f_max - 1) * n
# O(n) time O(n) space
#
# Maximum possible number of idle slots = (f_max - 1) * n
#   max_num_of_tasks_need_to_wait = f_max - 1, and wait time for each one of them is n

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Find the max frequency task
        cnt = Counter(tasks)
        max_freq_task, max_freq = max(cnt.items(), key=lambda x: x[1])

        # Initialize idle to be its highest possible value
        #   Also remove the max_freq_task from counter
        idle = n * (cnt.pop(max_freq_task) - 1)

        # Try squeeze other tasks while waiting for executing the max_freq_task
        for freq in cnt.values():
            idle -= min(freq, max_freq - 1)  # max # of gaps is max_freq - 1
            if idle <= 0:
                return len(tasks)

        return len(tasks) + idle

# class Solution:
#     def leastInterval(self, tasks: List[str], n: int) -> int:
#         frequencies = [0] * 26
#         for task in tasks:
#             frequencies[ord('A') - ord(task)] += 1

#         # Find the max frequency task and move it to frequencies[-1]
#         max_index = 0
#         for i in range(1, len(frequencies)):
#             if frequencies[i] > frequencies[max_index]:
#                 max_index = i
#         frequencies[max_index], frequencies[-1] = frequencies[-1], frequencies[max_index]

#         max_frequency = frequencies[-1]
#         idle_slots = n * (max_frequency - 1)
#         for i in range(len(frequencies) - 1): # for every other tasks
#             idle_slots -= min(frequencies[i], max_frequency - 1)
#             if idle_slots < 0:
#                 return len(tasks)


#         return len(tasks) + idle_slots