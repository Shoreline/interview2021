# Classic UnionFind class

# T O(NK * logNK);
# S O(NK): Here N is the number of accounts and K is the maximum length of an account.
# Classic UnionFind class
class UF:
    def __init__(self, N):
        # let self.parents[x] = x
        self.parents = list(range(N))

    def find(self, x):
        if self.parents[x] != x:
            # recursively call, eventually self.parents[x] = union_representative
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    # returns false if child and parent are already in the same union
    def union(self, child, parent):
        pc = self.find(child)
        pp = self.find(parent)

        if pc == pp:
            return False

        self.parents[pc] = pp
        return True
