# Note that the factors are set to be in the range [2, n - 1]
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        if n <= 1:
            return []

        res = []

        def dfs(tmp, rest, n):
            if len(tmp) > 0:
                res.append(tmp + [n])  # ex: [2, 6] is one of the results for 12.

            for i in range(rest, int(sqrt(n)) + 1):  # i <= target//i, i.e., i <= sqrt(target)
                if n % i == 0:  # i is a factor of n
                    tmp.append(i)
                    dfs(tmp, i, n // i)
                    tmp.pop()

        dfs([], 2, n)  # 2 is the smallest factor
        return res     