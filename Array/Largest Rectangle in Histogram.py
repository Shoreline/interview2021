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
# Maintain a strict ascending stack, that the top element stack[-1] is heights[i], which is the largest
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # The stack saves the index of previous biggest rectangle's right side (non-decreasing)
        res = 0

        # So the last element is 0, force stack to be empty (to ensure checking all possibilities) in the end
        heights.append(0)

        for i in range(len(heights)):
            # a constant in this while loop
            right = i - 1

            # Create a new rectangular that ends at i
            #   Check all possible big rectangles ends at i - 1
            #   For the poped indices, compute the areas of their rectangulars and update res
            #   Note the bar of heights[i] is not included! These rectangles end at heights[i-1] (inclusive)
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                left = 0 if len(stack) == 0 else stack[-1] + 1
                res = max(res, (right - left + 1) * h)

            stack.append(i)

        return res