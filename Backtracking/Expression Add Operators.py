# Each number can have multiple digits: ex we can slice "1234" into 12 * 3 + 4
#
# We use backtracking to generate all possible expressions by adding +, -, * to between the digits of s string.
# There is no priority since there are no parentheses ( and ) in our s string, so we can evaluate the expression on the fly to save time.
# There are total 3 operators:
# + operator: newResult = resSoFar + num
# - operator: newResult = resSoFar - num. # prevNum = -num!!
# * operator: newResult = resSoFar - prevNum + prevNum * num. We need to keep the prevNum so that to calculate newResult we need to minus prevNum then plus with prevNum * num. So newResult = resSoFar - prevNum + prevNum * num.

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:

        # cur is the currently computed value
        def dfs(tmp: list[str], start: int, cur: int, pre_num: int):
            if start == len(num):
                if cur == target:
                    res.append(''.join(tmp))
                return

            for i in range(start + 1, len(num) + 1):
                piece = num[start:i]  # [start,i) is the piece
                if len(piece) > 1 and piece[0] == '0':  # Skip leading zero number
                    break

                if start == 0:  # first piece, only + is possible
                    dfs(tmp + [piece], i, cur + int(piece), int(piece))
                else:
                    dfs(tmp + ["+", piece], i, cur + int(piece), int(piece))
                    dfs(tmp + ["-", piece], i, cur - int(piece), -int(piece))  # pre_num = negative piece!
                    dfs(tmp + ["*", piece], i, cur - pre_num + pre_num * int(piece), pre_num * int(piece))

        res = []
        dfs([], 0, 0, 0)
        return res