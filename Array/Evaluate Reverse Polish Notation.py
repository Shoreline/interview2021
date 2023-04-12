# Simply use a stack to save numbers need to be computed
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in "+-*/":     # can't use t.isdigit(), since '-11' is not a digit
                stack.append(int(t))
            else:
                r, l = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(l+r)
                elif t == "-":
                    stack.append(l-r)
                elif t == "*":
                    stack.append(l*r)
                else:
                    stack.append(int(l/r)) # can't use l // r, since int(6/-132) = 0, but 6 // -132 = -1
        return stack.pop()