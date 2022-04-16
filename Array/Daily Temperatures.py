# Use a stack to save array index
# Backward iteration. Have to go backward. Impossible to go forward since no one knows future temperature.
# stack has 1) value wise, decending order (the most top element stack[-1] has the smallest temperature[stack[-1]] in stack), saves future high temp days.
# 2) sequence wise, old -> new (the most top element stack[-1] is the newest index)
# stack: for each temperatures[i], keep poping stack until stack[-1] > temperatures[i]
# do stack.append(i) for each i
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        ans = [0] * n
        for i in range(n - 1, -1, -1):  # going from backwards
            while len(stack) > 0 and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            ans[i] = 0 if len(stack) == 0 else stack[-1] - i
            stack.append(i)

        return ans

    # My own solution without reading any reference
# O(n) time and O(n) space. But only faster than 23% and less than 14% of submissions
# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         stack = []
#         ans = [0] * len(temperatures)
#         for i in range(len(temperatures) - 1, -1, -1):
#             while len(stack) > 0 and temperatures[i] >= temperatures[stack[-1]]:
#                 stack.pop()
#             ans[i] = 0 if len(stack) == 0 else stack[-1] - i
#             stack.append(i)

#         return ans    