# Keep adding valid queens row by row.
# Once a valid queen is found, saves its 1) column number; 2) diagonal 1; 3) diagonal 2
#   No need to worry about conflicting rows since we add valid queens row by row (always on a new row)
#   1) is easy to record. The problem is how to label 2) and 3)
#   Note the two diagonals of a point (x,y) is y = x + b1 and y = -x + b2
#   So b1 and b2 can be used for labeling these diagonals.
class Solution:
    def totalNQueens(self, n: int) -> int:

        # queen_cols: a list, queen's column values
        # y: columns already occupied by queens of each row
        # xy_dif: diagonal 1
        # xy_sum: diagonal 2

        def dfs(cols_set: set[int], xy_dif: set[int], xy_sum: set[int]):
            nonlocal res
            x = len(cols_set)  # x is the row value of this to be added queen
            if x == n:  # Has reached the end
                res += 1
                return
            for y in range(n):
                if y not in cols_set and x - y not in xy_dif and x + y not in xy_sum:
                    cols_set.add(y)
                    xy_dif.add(x - y)
                    xy_sum.add(x + y)

                    dfs(cols_set, xy_dif, xy_sum)

                    cols_set.remove(y)
                    xy_dif.remove(x - y)
                    xy_sum.remove(x + y)

        res = 0
        dfs(set(), set(), set())

        return res