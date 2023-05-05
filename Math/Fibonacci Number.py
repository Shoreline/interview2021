class Solution:
    @lru_cache(None)
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1

        return self.fib(n - 1) + self.fib(n - 2)

# def fib(N):
# 	if N == 0: return 0
# 	memo = [0,1]
# 	for i in range(2,N+1):
# 		memo = [memo[-1], memo[-1] + memo[-2]]
#
# 	return memo[-1]