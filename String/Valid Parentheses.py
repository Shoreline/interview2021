class Solution:
    def isValid(self, s: str) -> bool:
        # Only need to insert the right brackets as the keys
        mapping = {")": "(", "}": "{", "]": "["}

        # use a List as Stack
        stack = []

        for c in s:
            if c in mapping:
                # If sees a right bracket, the first "pending" left bracket must be of the same kind. Otherwise
                # returns false.
                if len(stack) == 0 or stack[-1] != mapping[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)

        return len(stack) == 0

# Wrong solution. only check counts. "([)]" is not valid.
# class Solution:
#     def isValid(self, s: str) -> bool:
#         pairs = {')':'(', ']':'[', '}':'{'}
#         mp_left = collections.defaultdict(int)

#         for c in s:
#             if c in '({[':
#                 mp_left[c] += 1
#             else:
#                 mp_left[pairs[c]] -= 1
#                 if mp_left[pairs[c]] < 0:
#                     return False

#         for cnt in mp_left.values():
#             if cnt > 0:
#                 return False

#         return True


