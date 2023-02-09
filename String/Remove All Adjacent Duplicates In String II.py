# Save the character c and its count to the stack.
# If the next character c is same as the last one, increment the count.
# Otherwise, push a pair (c, 1) into the stack.

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack and stack[-1][0] == c and stack[-1][1] == k - 1:
                stack.pop()
            else:
                if not stack or stack[-1][0] != c:
                    stack.append([c, 1])
                else:
                    stack[-1][1] += 1

        return ''.join([x[0] * x[1] for x in stack])