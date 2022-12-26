class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def dfs(pos, k, target, tmp):
            if k == 0 and target == 0:
                res.append(tmp[:])
                return
            if k < 0 or target < 0:
                return
            
            for i in range(pos, 10):
                tmp.append(i)
                dfs(i+1, k-1, target -i, tmp)
                tmp.pop()
            
        dfs(1, k, n, [])
        return res
