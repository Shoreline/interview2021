# Note that the factors are set to be in the range [2, n - 1]
#   In math, factors shall be [1, n]
# factor doesn't have to be a prime!
# factor can be reused.
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        if n <= 1:
            return []

        res = []

        def dfs(tmp, min_factor, n):
            if tmp:  # if tmp is not empty, then we have found a combination.
                res.append(tmp + [n])  # ex: [2, 6] is one of the results for 12.

            for i in range(min_factor, int(sqrt(n)) + 1):  # i <= target//i, i.e., i <= sqrt(target)
                if n % i == 0:  # i is a factor of n
                    tmp.append(i)
                    dfs(tmp, i, n // i)
                    tmp.pop()

        dfs([], 2, n)  # 2 is the smallest factor
        return res
