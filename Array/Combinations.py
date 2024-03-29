# Backtracking
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def bt(start, k, tmp):
            #  nonlocal n
            if k == 0:
                if len(tmp) > 0:
                    res.append(tmp[:])
                return
            if n - start + 1 < k:
                return
            for i in range(start, n + 1):
                tmp.append(i)
                bt(i + 1, k - 1, tmp)
                tmp.pop()

        bt(1, k, [])
        return res

# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         res = []
#
#         def dfs(start, end, k, tmp):
#             if k == 0:
#                 res.append(tmp[:])
#                 return
#
#             for i in range(start, end + 1):
#                 tmp.append(i)
#                 dfs(i + 1, end, k - 1, tmp)
#                 tmp.pop()
#
#         dfs(1, n, k, [])
#         return res

# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         res = []
#
#         def dfs(num: int, n: int, k: int, tmp: list[int]):
#             if k == 0:
#                 res.append(tmp[:])
#                 return
#
#             for i in range(num, n + 1):
#                 tmp.append(i)
#                 dfs(i + 1, n, k - 1, tmp)  # i+1, not num+1 !
#                 tmp.pop()
#
#         dfs(1, n, k, [])
#         return res