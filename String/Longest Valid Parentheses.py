# Stack[i] after poping for a right bracket: saves the starting index of the next POSSIBLE valid substring,
# excluding s[stack[i]]
#   - Node that a valid substring can only start with a LEFT bracket
# stack is implemented by list in Python
# T/S: O(n): n is the length of the given string

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        # stack saves "one index before the next POSSIBLE valid substring"
        stack = [-1]  # Initialized with -1

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:  # this will happen if there is more ')' than '('
                    stack.append(i)
                else:
                    # the valid substring is from s[stack[-1]] + 1 to i
                    # to be more specific: i - (stack[-1] + 1) + 1 = i - stack[-1]
                    res = max(res, i - stack[-1])
        return res


class Solution2:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        stack = [0]

        for i in range(len(s)):
            if s[i] == '(':  # when s[i] is the top element of the stack, the next valid substring starts from i + 1
                stack.append(i + 1)
            else:
                print('stack', stack)
                stack.pop()  # always pop() when possible
                print('stack2', stack)
                if len(stack) == 0:  # Seeing multiple right brackets. It means no valid substring can cross s[i].
                    # The problem becomes keep looking for LVP for s[i+1:]
                    stack.append(i + 1)
                else:  # a valid substring is found
                    res = max(res, i - stack[-1] + 1)
        return res

# Using a stack to push/pop LEFT brackets.
# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         if(len(s)==0):
#             return 0

#         stack = [] # saves indice of the left brackets that are still "pending" to match a right bracket
#         valid_start_while_empty = 0 # an additional variable to save the valid starting index while stack is empty
#         res = 0

#         for i in range(len(s)):
#             if s[i] == '(':
#                 stack.append(i)
#             else:
#                 if len(stack) == 0:  # Making previous substring invalid, so need to reset valid_start_while_empty
#                     valid_start_while_empty = i + 1 # actually, valid_start_while_empty is at least i+1
#                 else:
#                     stack.pop()
#                     if len(stack) == 0:
#                         res = max(res, i - valid_start_while_empty + 1)
#                     else: # From s[stack[-1]] + 1 to i is a valid string
#                         # to be more specific: i - (stack[-1] + 1) + 1 = i - stack[-1]
#                         res = max(res, i - stack[-1])

#         return res