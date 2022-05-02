# Nested iterations, no need to do recursion.
class Solution:
    def countAndSay(self, n: int) -> str:
        if n < 1:
            return ""

        tmp = []
        s = "1"
        for i in range(n - 1):  # Total run is n times. But the first run is already done by setting s = "1"
            count = 1
            for j in range(len(s)):
                if j + 1 < len(s) and s[j] == s[j + 1]:
                    count += 1
                else:
                    tmp.append(str(count))
                    tmp.append(s[j])
                    count = 1  # reset count
            s = "".join(tmp)
            tmp.clear()

        return s

