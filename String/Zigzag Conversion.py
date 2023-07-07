# Construct the result string directly.
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if (numRows == 1):
            return s

        res = ''
        step = 2 * numRows - 2  # note that step will be 0 when numRows is 1, so need to deal with it separately

        for row_num in range(numRows):
            j = 0
            while j + row_num < len(s):
                res += s[
                    j + row_num]  # row_num is also the starting index of s for all characters in that row for the new zigzag string

                # For inner rows, add one more character before jumping to next cycle
                # The 2nd character can be reached after numRows - row_num indice
                if row_num != 0 and row_num != numRows - 1:  # inner row
                    if j + step - row_num < len(s):
                        res += s[j + step - row_num]
                j += step

        return res
