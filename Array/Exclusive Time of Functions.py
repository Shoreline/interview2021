# The tricky part is that when a function is interrupted, no direct log for that.

# Straightforward iteration & stack
# easy to forgot +1 time when event is ending
# An end event 1) can only ends the ongoing task; 2) automatically resume previous task
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n  # array index is function_id
        stack = []  # stack element: [function_id, previous_start_time]
        for log in logs:
            function_id, event, time = log.split(':')  # new log
            function_id, time = int(function_id), int(time)

            if event == 'start':  # a new function overrides the running one. So count how much time the running one has run
                if stack:
                    # res[stack[-1][0]] += time-stack[-1][1]
                    running_f_id = stack[-1][0]
                    running_time = time - stack[-1][1]  # running time doesn't include the current second
                    res[running_f_id] += running_time
                stack.append([function_id, time])  # add the info of the new function
            else:  # Curret event ends, meanwhile don't forget it also means the next event in stack is restarted
                finished_f = stack.pop()
                res[finished_f[0]] += (time - finished_f[1] + 1)  # time is inclusive, so + 1
                if stack:
                    stack[-1][
                        1] = time + 1  # the next event in the stack starts running again from the next time slot (time + 1)

        return res

    # class Solution:
#     def exclusiveTime(self, n, logs):
#         ans, stack = [0]*n, []
#         for log in logs:
#             f_id, event, time = log.split(':')
#             f_id, time = int(f_id), int(time)
#             if event=='start':
#                 if stack:
#                     ans[stack[-1][0]] += time-stack[-1][1]
#                 stack.append([f_id, time])
#             else:
#                 popped = stack.pop()
#                 ans[popped[0]] += time-popped[1]+1
#                 if stack:
#                     stack[-1][1] = time+1
#         return ans