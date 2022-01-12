# Elements in candidates may have repeated value. Also one result can have repeated value.
# key: i > pos and candidates[i] == candidates[i - 1]: continue
#   For elements of the same value, don't repeat neither picking/dropping, just skip it.
#   Not saying both elements of the same value can't be in a result array at the same time.
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(target: int, pos: int, tmp: list[int]):
            if target == 0:
                res.append(tmp[:])
                return
            if target < 0:
                return

            for i in range(pos, len(candidates)):
                if i > pos and candidates[i] == candidates[i - 1]:
                    continue

                tmp.append(candidates[i])
                dfs(target - candidates[i], i + 1, tmp)
                tmp.pop()

        dfs(target, 0, [])
        return res
