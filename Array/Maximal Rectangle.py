# Convert into the problem of Largest Rectangle in Histogram#
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        # Let length be len(matrix[0]) + 1, so the last element is 0,
        # force stack to be empty (to ensure checking all possibilities) in the end
        heights = [0] * (len(matrix[0]) + 1)
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heights[j] = 0 if matrix[i][j] == '0' else heights[j] + 1
            res = max(res, self.largestRectangleArea(heights))
        return res

    # Slightly different than the solution of largest rectangle in histogram
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i in range(len(heights)):
            # Check all possible bigger rectangles
            while len(stack) > 0 and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                right = i - 1
                left = 0 if len(stack) == 0 else stack[-1] + 1
                res = max(res, (right - left + 1) * h)

            stack.append(i)

        return res