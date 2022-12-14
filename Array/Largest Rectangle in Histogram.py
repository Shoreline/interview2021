# /*
#  * not the most concise one, but more straightforward
#  *
#  * The stack saves the index of previous rectangle's right side. So its left
#  * side index is stack.pop().peek() + 1. Also, this is not the rectangle we
#  * want to use! The one we want to use has its right side of index i-1
#  *
#  * Use the extended height array reduced code complexity
#  */

# t&s: O(n)
# stack is a descending array
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # The stack saves the index of previous biggest rectangle's right side (non-decreasing)
        res = 0

        # So the last element is 0, force stack to be empty (to ensure checking all possibilities) in the end
        heights.append(0)

        for i in range(len(heights)):
            # Check all possible bigger rectangles
            while len(stack) > 0 and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                right = i - 1  # a constant in this while loop
                left = 0 if len(stack) == 0 else stack[-1] + 1
                res = max(res, (right - left + 1) * h)

            stack.append(i)

        return res