# Keep adding valid queens row by row.
# Once a valid queen is found, saves its 1) column number; 2) diagonal 1; 3) diagonal 2
#   No need to worry about conflicting rows since we add valid queens row by row (always on a new row)
#   1) is easy to record. The problem is how to label 2) and 3)
#   Note the two diagonals of a point (x,y) is y = x + b1 and y = -x + b2
#   So b1 and b2 can be used for labeling these diagonals.
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        # queens: columns already occupied by queens of each row
        # xy_dif: diagonal 1
        # xy_sum: diagonal 2
        def dfs(queen_cols: list[int], xy_dif: list[int], xy_sum: list[int]):
            x = len(queen_cols)  # x is the index of the next row
            if x == n:
                result.append(queen_cols)
                return
            for y in range(n):
                if y not in queen_cols and x - y not in xy_dif and x + y not in xy_sum:
                    dfs(queen_cols + [y], xy_dif + [x - y], xy_sum + [x + y])

        result = []
        dfs([], [], [])

        res = []
        for queen_cols in result:
            a_res = []
            for queen_col in queen_cols:
                row = ["."] * n
                row[queen_col] = 'Q'
                a_res.append(''.join(row))
            res.append(a_res[:])
        return res

        # Or, use below instead
        # return [ ["."*i + "Q" + "."*(n-i-1) for i in queen_cols] for queen_cols in result]