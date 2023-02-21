class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            res.append([])
            for j in range(i + 1):
                val = 0
                if j == 0:
                    val = res[-2][0]
                elif j == i:
                    val = res[-2][-1]
                else:
                    val = res[-2][j-1] + res[-2][j]
                res[-1].append(val)
        return res

# class Solution:
#     def generate(self, num_rows: int) -> List[List[int]]:
#         triangle = []
#
#         for row_num in range(num_rows):
#             # The first and last row elements are always 1.
#             # row = [None for _ in range(row_num + 1)] # next level will have row_num + 1 elements
#             row = [0] * (row_num + 1)
#             row[0], row[-1] = 1, 1
#
#             # Each triangle element is equal to the sum of the elements
#             # above-and-to-the-left and above-and-to-the-right.
#             for j in range(1, len(row) - 1):
#                 row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
#
#             triangle.append(row)
#
#         return triangle

    # class Solution:
#     def generate(self, numRows: int) -> List[List[int]]:
#         res = []

#         def helper(n:int, pre_lvl:list[int]):
#             if n == 0:
#                 return

#             tmp = [1]
#             for i in range(len(pre_lvl) - 1):
#                 tmp.append(pre_lvl[i] + pre_lvl[i+1])

#             if pre_lvl:
#                 tmp.append(1)

#             res.append(tmp)

#             helper(n - 1, tmp)

#         helper(numRows, [])
#         return res


