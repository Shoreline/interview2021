class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def dfs(pos: int, tmp: list[str]):
            if pos == len(s) and len(tmp) == 4:
                res.append(".".join(tmp))
                return
            elif len(tmp) > 4:
                return

            for i in range(pos, pos + 3):
                if i >= len(s):
                    continue
                if i > pos and s[pos] == '0':
                    continue
                if i == pos + 2 and int(s[pos:i + 1]) > 255:
                    continue

                tmp.append(s[pos: i + 1])
                dfs(i + 1, tmp)
                tmp.pop()

        dfs(0, [])
        return res
