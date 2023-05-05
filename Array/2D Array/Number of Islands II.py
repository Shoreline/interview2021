class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        # Returns the cell representing an island
        def find(cell):
            while cell in cell_paths:
                # path compression
                if cell_paths[cell] in cell_paths:
                    cell_paths[cell] = cell_paths[cell_paths[cell]]
                cell = cell_paths[cell]
            return cell

        # Tries to unite two input cells.
        #   Note that we only call this function for two neighboring cells.
        # If they already belong to the same island, returns False
        def union(c1,c2):
            pa1, pa2 = find(c1), find(c2)
            if pa1 == pa2: # union fail, cells are already united.
                return False

            cell_paths[pa1] = pa2 # connect two representitive cells
            return True

        seen, cell_paths, count = set(), {}, 0
        res = []
        for x,y in positions:
            # #island += 1 for any new island
            # Then check any neighboring cell that is part of an existing island
            # if union success, cur cell only extends an existing island -> #island -= 1.
            if (x,y) not in seen:
                seen.add((x,y))
                count += 1
                for x2,y2 in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                    # If a neighbor cell (x2, y2) is part of an island (in seen),
                    # try to unite it with this cell (x,y)
                    if (x2, y2) in seen and union((x,y), (x2, y2)):
                        count -= 1
            res.append(count)

        return res