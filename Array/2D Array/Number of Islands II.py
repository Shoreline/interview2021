# Must go through union-find, since one new island can reduce # island by more than one:
#   X O X
#   O X O   // O represents island. If flip the middle cell to be island, then #island dropped from 4 to just 1.
#   X O X

# Note: there is no island at the beginning, all water
# land in positions array is added one after another. The earlier added land will stay.
# time complexity: O(m * n + l) l: size of positions
# space: O(m * n)
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        # Returns the island for a cell. Actually the island is represented by its first land cell
        #   This cell is the first land cell of this island
        def find(cell):
            while cell in cell_paths:
                # path compress, optional but more efficient
                # Update cell_paths so each cell points the first land of the island,
                # instead of its adjacent land cell
                if cell_paths[cell] in cell_paths:
                    cell_paths[cell] = cell_paths[cell_paths[cell]]

                cell = cell_paths[cell]
            return cell

            # Tries to unite two input cells.

        # Note that we only call this function for two neighboring cells.
        # If they already belong to the same island, returns False
        def union(c1, c2):
            pa1, pa2 = find(c1), find(c2)
            if pa1 == pa2:  # union fail, cells are already in the same union.
                return False

            cell_paths[pa1] = pa2  # connect two islands. cell_paths[pa2] = pa1 also works
            return True

        land, cell_paths, count = set(), {}, 0
        res = []
        # connect with 4 adjacent cell,if land & union success, then one less island.
        for x, y in positions:
            if (x, y) not in land:
                land.add((x, y))
                count += 1
                for x2, y2 in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    # If a neighbor cell (x2, y2) is part of an island (in seen),
                    # try to unite it with this cell (x,y)
                    if (x2, y2) in land and union((x, y), (x2, y2)):
                        count -= 1

            res.append(count)

        return res