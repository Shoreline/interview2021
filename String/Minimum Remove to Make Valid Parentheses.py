# stack
# stack to save '(' index only. Push for any '(', pop for ')'. If stack is empty and sees a ')' then remove that ')'
# After iterating through the whole string, remaining '(' in the stack shall also be removed
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        illegal = set()
        stack = []  # only save indice of '('
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    illegal.add(i)

                    # remaining unmatched left parentheses '(' are also illegal
        illegal = illegal.union(set(stack))  # cannot just illegal.union(set(stack))

        res = []
        for i in range(len(s)):
            if i not in illegal:
                res.append(s[i])

        return "".join(res)
