# The key here is to realize that the sum of indices on all diagonals are equal.
#   -> One diagonal can be uniquely represented by x + y, with any cell (x,y) on it.

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        d = collections.defaultdict(list)
        # loop through matrix
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                # keep adding elements to index_sum (i + j)
                # Note that when (i + j) is odd the elements are added as expected order
                # But when (i + j) is even, the elements are added as the reverse order
                d[i + j].append(mat[i][j])

            # we're done with the pass, let's build our answer array
        ans = []
        # look at the diagonal and each diagonal's elements
        # d's items are in the order of key insertion -> sorted by key!
        for k, v in d.items():
            # each entry looks like (diagonal level (sum of indices), [elem1, elem2, elem3, ...])
            # snake time, look at the diagonal level
            if k % 2 == 0:
                # Here we append in reverse order because its an even numbered level/diagonal.
                [ans.append(x) for x in v[::-1]]
            else:
                [ans.append(x) for x in v[::]]

        return ans        