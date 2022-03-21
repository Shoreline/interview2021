# Only +-*, no /

class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        @lru_cache()
        def dfs(exp: str) -> list[int]:
            if exp.isdigit():
                return [int(exp)]

            res = []
            for i in range(len(exp)):
                if exp[i] in '+-*':
                    left = dfs(exp[:i])
                    right = dfs(exp[i + 1:])

                    for l in left:
                        for r in right:
                            res.append(eval(str(l) + exp[i] + str(r)))
            return res

        return dfs(expression)
