# copied

# idea:
#   each row in input array is independent and can be processed separately
# how to process each row:
#   we need to move stones ("#") to empty spaces (".") from left to right
#   since it's only move from left to right, we can iterate from the end of the row
#   and keep in memory the last non-obstacle space where we can move stones
# and at the end we just need to rotate array

# possible_cell and i are two pointers row[possible_cell] is a POSSIBLE empty cell, but not necessarily true. It is on
# the left of a certainly not available cell (obstacle or dropped stone)

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for row in box:  # each row can be processed separately
            avl_ptr = len(row) - 1  # actually it's the potential available spot
            for i in range(len(row) - 1, -1, -1):
                # no need to update possible_cell while seeing an empty cell.
                if row[i] == '#':  # if stone, move it to the "possible_cell"
                    if i < avl_ptr:
                        row[i], row[avl_ptr] = row[avl_ptr], row[i]
                    avl_ptr -= 1
                elif row[i] == '*':  # if obstacle, we cannot move stones behind obstacles
                    avl_ptr = i - 1

        # return zip(*box[::-1])   # some fancy rotating method
        rotated = [[0] * len(box) for _ in range(len(box[0]))]  # switch row/col as box
        for i in range(len(box)):
            for j in range(len(box[0])):
                rotated[j][len(box) - 1 - i] = box[i][j]
        return rotated
#         rotate = []
#         for i in range(len(box[0])):
#             rotate.append([])
#             for j in range(len(box) - 1, -1, -1):
#                 rotate[i].append(box[j][i])

#         return rotate

# class Solution:
#     def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
#         for row in box: # each row can be processed seprately
#             possilbe_cell = len(row) - 1             # initialize with the last index in row

#             for i in range(len(row) - 1, -1, -1):    # iterate from the end of the row
#                 # no need to update possible_cell while seeing an empty cell.
#                 if row[i] == "*":                    # if obstacle, we cannot move stones behind obstacles
#                     possilbe_cell = i - 1            #  so update possilbe_cell to the first before obstacle
#                 elif row[i] == "#":                  # if stone, move it to the "possilbe_cell"
#                     row[possilbe_cell], row[i] = row[i], row[possilbe_cell] # It's possible that possilbe_cell = i
#                     possilbe_cell -= 1

#         #return zip(*box[::-1])   # some fancy rotating method
#         rotate = []
#         for i in range(len(box[0])):
#             rotate.append([])
#             for j in range(len(box) - 1, -1, -1):
#                 rotate[i].append(box[j][i])

#         return rotate        